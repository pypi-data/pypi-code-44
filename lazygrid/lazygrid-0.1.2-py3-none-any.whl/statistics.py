# -*- coding: utf-8 -*-
#
# Copyright 2019 Pietro Barbiero and Giovanni Squillero
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
from typing import Union, Callable

from scipy import stats
from scipy.stats import mannwhitneyu

from sklearn.datasets import make_classification
from sklearn.linear_model import RidgeClassifier, LogisticRegression
from sklearn.metrics import confusion_matrix


def confidence_interval_mean_t(x: np.ndarray, cl: float = 0.05) -> tuple([float, float]):
    """
    Compute the confidence interval of the mean from sample data.

    Examples
    --------
    >>> import numpy as np
    >>>
    >>> np.random.seed(42)
    >>> x = np.random.normal(loc=0, scale=2, size=10)
    >>> confidence_level = 0.05
    >>>
    >>> confidence_interval_mean_t(x, confidence_level)
    (-0.13829578539063092, 1.9305402321856557)


    Notes
    --------
    You should use the t distribution rather than the normal distribution
    when the variance is not known and has to be estimated from sample data.

    When the sample size is large, say 100 or above, the t distribution
    is very similar to the standard normal distribution.
    However, with smaller sample sizes, the t distribution is leptokurtic,
    which means it has relatively more scores in its tails than does the normal distribution.
    As a result, you have to extend farther from the mean to contain a given proportion of the area.

    Parameters
    --------
    :param x: sample
    :param cl: confidence level
    :return: confidence interval
    """

    if np.all(x == np.mean(x)):
        return 2 * [np.mean(x)]
    return stats.t.interval(1-cl, len(x)-1, loc=np.mean(x), scale=stats.sem(x))


def find_best_solution(solutions: list,
                       test: Callable = mannwhitneyu,
                       alpha: float = 0.05,
                       **kwargs) -> (int, list, list):
    """
    Find the best solution in a list of candidates, according to
    a statistical test and a significance level (alpha).

    The best solution is defined as the one having the highest mean value.

    Examples
    --------
    >>> from sklearn.linear_model import LogisticRegression, RidgeClassifier
    >>> from sklearn.ensemble import RandomForestClassifier
    >>> from sklearn.datasets import make_classification
    >>> from sklearn.model_selection import cross_val_score
    >>>
    >>> x, y = make_classification(random_state=42)
    >>>
    >>> model1 = LogisticRegression(random_state=42)
    >>> model2 = RandomForestClassifier(random_state=42)
    >>> model3 = RidgeClassifier(random_state=42)
    >>> model_names = ["LogisticRegression", "RandomForestClassifier", "RidgeClassifier"]
    >>>
    >>> score1 = cross_val_score(estimator=model1, X=x, y=y, cv=10)
    >>> score2 = cross_val_score(estimator=model2, X=x, y=y, cv=10)
    >>> score3 = cross_val_score(estimator=model3, X=x, y=y, cv=10)
    >>>
    >>> scores = [score1, score2, score3]
    >>> best_idx, best_solutions_idx, pvalues = find_best_solution(scores)
    >>> model_names[best_idx]
    'LogisticRegression'
    >>> best_solutions_idx
    [0, 2]
    >>> pvalues #doctest: +ELLIPSIS
    [0.4782..., 0.0360..., 0.1610...]

    Parameters
    --------
    :param solutions: list of candidate solutions
    :param test: statistical test
    :param alpha: significance level
    :param kwargs: additional parameters required by the statistical test
    :return: a tuple containing:
        - the position of the best solution inside the candidate input list;
        - the positions of the solutions which are not separable from the best one;
        - the list of p-values returned by the statistical test while comparing the best solution to the other candidates
    """

    best_idx = 0
    best_solution = solutions[best_idx]
    best_mean = np.mean(best_solution)

    # find the best solution (the one having the highest mean value)
    index = 1
    for solution in solutions[index:]:
        solution_mean = np.mean(solution)

        if solution_mean > best_mean:
            best_solution = solution
            best_mean = np.mean(best_solution)
            best_idx = index

        index += 1

    best_solutions_idx = []
    pvalues = []

    # check if there are other candidates which may be equivalent to the best one
    index = 0
    for solution in solutions:
        try:
            statistic, pvalue = test(best_solution, solution, **kwargs)
        except ValueError:
            statistic, pvalue = np.inf, np.inf

        if pvalue > alpha:
            best_solutions_idx.append(index)
        pvalues.append(pvalue)

        index += 1

    return best_idx, best_solutions_idx, pvalues


def confusion_matrix_aggregate(fitted_models, x, y):

    y_pred_list = []
    y_list = []
    for model in fitted_models:
        y_pred = model.predict(x)
        y_pred_list.append(y_pred)
        y_list.append(y)
    y_pred_list = np.concatenate(y_pred_list, axis=0)
    y_list = np.concatenate(y_list, axis=0)
    conf_mat = confusion_matrix(y_list, y_pred_list)
    conf_mat = np.rot90(conf_mat, 2).T

    return conf_mat
