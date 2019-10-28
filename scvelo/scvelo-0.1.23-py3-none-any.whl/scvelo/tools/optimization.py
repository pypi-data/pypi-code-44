from .utils import sum_obs, prod_sum_obs, make_dense
from scipy.optimize import minimize
from scipy.sparse import csr_matrix, issparse
import numpy as np
import warnings


def get_weight(x, y=None, perc=95):
    xy_norm = np.array(x.A if issparse(x) else x)
    if y is not None:
        if issparse(y): y = y.A
        xy_norm = xy_norm / np.clip(np.max(xy_norm, axis=0), 1e-3, None)
        xy_norm += y / np.clip(np.max(y, axis=0), 1e-3, None)
    if isinstance(perc, int):
        weights = xy_norm >= np.percentile(xy_norm, perc, axis=0)
    else:
        lb, ub = np.percentile(xy_norm, perc, axis=0)
        weights = (xy_norm <= lb) | (xy_norm >= ub)
    return weights


def leastsq_NxN(x, y, fit_offset=False, perc=None):
    """Solution to least squares: gamma = cov(X,Y) / var(X)
    """
    if perc is not None:
        if not fit_offset and isinstance(perc, (list, tuple)): perc = perc[1]
        weights = csr_matrix(get_weight(x, y, perc=perc)).astype(bool)
        x, y = weights.multiply(x).tocsr(), weights.multiply(y).tocsr()
    else:
        weights = None

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        xx_ = prod_sum_obs(x, x)
        xy_ = prod_sum_obs(x, y)

        if fit_offset:
            n_obs = x.shape[0] if weights is None else sum_obs(weights)
            x_ = sum_obs(x) / n_obs
            y_ = sum_obs(y) / n_obs
            gamma = (xy_ / n_obs - x_ * y_) / (xx_ / n_obs - x_ ** 2)
            offset = y_ - gamma * x_

            # fix negative offsets:
            idx = offset < 0
            gamma[idx] = xy_[idx] / xx_[idx]
            offset = np.clip(offset, 0, None)
        else:
            gamma = xy_ / xx_
            offset = np.zeros(x.shape[1])
    offset[np.isnan(offset)], gamma[np.isnan(gamma)] = 0, 0
    return offset, gamma


def optimize_NxN(x, y, fit_offset=False, perc=None):
    """Just to compare with closed-form solution
    """
    if perc is not None:
        if not fit_offset and isinstance(perc, (list, tuple)): perc = perc[1]
        weights = get_weight(x, y, perc).astype(bool)
        if issparse(weights): weights = weights.A
    else:
        weights = None

    x, y = x.astype(np.float64), y.astype(np.float64)

    n_vars = x.shape[1]
    offset, gamma = np.zeros(n_vars), np.zeros(n_vars)

    for i in range(n_vars):
        xi = x[:, i] if weights is None else x[:, i][weights[:, i]]
        yi = y[:, i] if weights is None else y[:, i][weights[:, i]]

        if fit_offset:
            offset[i], gamma[i] = minimize(lambda m: np.sum((-yi + xi * m[1] + m[0])**2), method="L-BFGS-B",
                                           x0=(0, 0.1), bounds=[(0, None), (None, None)]).x
        else:
            gamma[i] = minimize(lambda m: np.sum((-yi + xi * m) ** 2), x0=0.1, method="L-BFGS-B").x
    offset[np.isnan(offset)], gamma[np.isnan(gamma)] = 0, 0
    return offset, gamma


def leastsq_generalized(x, y, x2, y2, res_std=None, res2_std=None, fit_offset=False, fit_offset2=False, perc=None):
    """Solution to the 2-dim generalized least squares: gamma = inv(X'QX)X'QY
    """
    if perc is not None:
        if not fit_offset and isinstance(perc, (list, tuple)): perc = perc[1]
        weights = csr_matrix(get_weight(x, y, perc=perc) | get_weight(x, perc=perc)).astype(bool)
        x, y = weights.multiply(x).tocsr(), weights.multiply(y).tocsr()

    n_obs, n_var = x.shape
    offset, offset_ss = np.zeros(n_var, dtype="float32"), np.zeros(n_var, dtype="float32")
    gamma = np.ones(n_var, dtype="float32")

    if (res_std is None) or (res2_std is None): res_std, res2_std = np.ones(n_var), np.ones(n_var)
    ones, zeros = np.ones(n_obs), np.zeros(n_obs)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        x, y = np.vstack((make_dense(x)/res_std, x2/res2_std)), np.vstack((make_dense(y)/res_std, y2/res2_std))

    if fit_offset and fit_offset2:
        for i in range(n_var):
            A = np.c_[np.vstack((np.c_[ones/res_std[i], zeros], np.c_[zeros, ones/res2_std[i]])), x[:, i]]
            offset[i], offset_ss[i], gamma[i] = np.linalg.pinv(A.T.dot(A)).dot(A.T.dot(y[:, i]))
    elif fit_offset:
        for i in range(n_var):
            A = np.c_[np.hstack((ones/res_std[i], zeros)), x[:, i]]
            offset[i], gamma[i] = np.linalg.pinv(A.T.dot(A)).dot(A.T.dot(y[:, i]))
    elif fit_offset2:
        for i in range(n_var):
            A = np.c_[np.hstack((zeros, ones/res2_std[i])), x[:, i]]
            offset_ss[i], gamma[i] = np.linalg.pinv(A.T.dot(A)).dot(A.T.dot(y[:, i]))
    else:
        for i in range(n_var):
            A = np.c_[x[:, i]]
            gamma[i] = np.linalg.pinv(A.T.dot(A)).dot(A.T.dot(y[:, i]))

    offset[np.isnan(offset)] = 0
    offset_ss[np.isnan(offset_ss)] = 0
    gamma[np.isnan(gamma)] = 0

    return offset, offset_ss, gamma


def maximum_likelihood(Ms, Mu, Mus, Mss, fit_offset=False, fit_offset2=False):
    """Maximizing the log likelihood using weights according to empirical bayes
    """
    n_obs, n_var = Ms.shape
    offset, offset_ss = np.zeros(n_var, dtype="float32"), np.zeros(n_var, dtype="float32")
    gamma = np.ones(n_var, dtype="float32")

    def sse(A, data, b):
        sigma = (A.dot(data) - b).std(1)
        return np.log(sigma).sum()  # np.log(np.sqrt(2*np.pi) * sigma).sum() + (.5 * (res/sigma[:, None])**2).sum()

    if fit_offset and fit_offset2:
        for i in range(n_var):
            data = np.vstack((Mu[:, i], Ms[:, i], Mus[:, i], Mss[:, i]))
            offset[i], offset_ss[i], gamma[i] = \
                minimize(lambda m: sse(np.array([[1, -m[2], 0, 0], [1, m[2], 2, -2 * m[2]]]),
                                       data, b=np.array(m[0], m[1])), x0=(1e-4, 1e-4, 1), method="L-BFGS-B").x
    elif fit_offset:
        for i in range(n_var):
            data = np.vstack((Mu[:, i], Ms[:, i], Mus[:, i], Mss[:, i]))
            offset[i], gamma[i] = \
                minimize(lambda m: sse(np.array([[1, -m[1], 0, 0], [1, m[1], 2, -2 * m[1]]]),
                                       data, b=np.array(m[0], 0)), x0=(1e-4, 1), method="L-BFGS-B").x
    elif fit_offset2:
        for i in range(n_var):
            data = np.vstack((Mu[:, i], Ms[:, i], Mus[:, i], Mss[:, i]))
            offset_ss[i], gamma[i] = \
                minimize(lambda m: sse(np.array([[1, -m[1], 0, 0], [1, m[1], 2, -2 * m[1]]]),
                                       data, b=np.array(0, m[0])), x0=(1e-4, 1), method="L-BFGS-B").x
    else:
        for i in range(n_var):
            data = np.vstack((Mu[:, i], Ms[:, i], Mus[:, i], Mss[:, i]))
            gamma[i] = \
                minimize(lambda m: sse(np.array([[1, -m, 0, 0], [1, m, 2, -2 * m]]), data, b=0),
                         x0=gamma[i], method="L-BFGS-B").x
    return offset, offset_ss, gamma
