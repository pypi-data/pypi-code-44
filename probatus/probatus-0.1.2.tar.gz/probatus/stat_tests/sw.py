import pandas as pd
import random
from scipy import stats
from ..utils import assure_numpy_array

def sw(d1, d2, verbose = False):
    """
    Examines whether deviation from normality of two distributions are significantly different. By using Shapiro-Wilk test
    as the basis
    Args:
        d1 (np.ndarray or pd.core.series.Series) : first sample
        d2 (np.ndarray or pd.core.series.Series) : second sample
        verbose (bool)                           : helpful interpretation msgs printed to stdout (default False)

    Returns:
        delta (float)     : test statistic defined as difference between two Shapiro-Wilk statistics
        pvalue (float) : P value of rejecting the null hypothesis (that the two distributions are identical)
    """

    d1 = assure_numpy_array(d1)
    d2 = assure_numpy_array(d2)


    if len(d1) > 5000:
        d1 = pd.Series(random.choices(d1, k=5000))
    if len(d2) > 5000:
        d2 = pd.Series(random.choices(d2, k=5000))

    delta = stats.shapiro(d1)[0] - stats.shapiro(d2)[0]

    d1 = pd.Series(d1)
    d2 = pd.Series (d2)
    
    MOT = pd.concat([d1,d2])
    n1 = d1.shape[0]  
    n2 = d2.shape[0]

    def ran_delta(n1, n2):
        take_ran = lambda n: random.sample(range(MOT.shape[0]), n)
        ran_1 = MOT.iloc[take_ran(n1),]
        ran_2 = MOT.iloc[take_ran(n2),]
        delta_ran = stats.shapiro(ran_1)[0] - stats.shapiro(ran_2)[0]
        return delta_ran

    collect = [ran_delta(n1, n2) for a in range(100)]
    collect = pd.Series(list(collect))
    delta_p_value = 1-stats.percentileofscore(collect,delta)/100

    quants = [0.025, 0.975]
    sig_vals = list(collect.quantile(quants))
    
    if verbose: 

        if delta < sig_vals[0] or delta > sig_vals[1]:
            print('\nShapiro_Difference | Null hypothesis : <delta is not different from zero> REJECTED.')
            print('\nDelta is outside 95% CI -> Distributions very different.')
        else:
            print('\nShapiro_Difference | Null hypothesis : <delta is not different from zero> NOT REJECTED.')
            print('\nDelta is inside 95% CI -> Distributions are not different.')

    return delta, delta_p_value
