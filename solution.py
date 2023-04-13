import pandas as pd
import numpy as np
from scipy.stats import ttest_ind


chat_id = 845786312 # Ваш chat ID, не меняйте название переменной

def solution(x:np.array, y:np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    res = ttest_ind(x, y)
    return res[1] < 0.03
