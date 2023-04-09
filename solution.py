import pandas as pd
import numpy as np
from scipy import stats


chat_id = 700385968 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    pval = stats.mannwhitneyu(x, y).pvalue
    if (pval < 0.1):
      ans = True
    else:
      ans = False
    return ans
