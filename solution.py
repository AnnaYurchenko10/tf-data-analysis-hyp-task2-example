import pandas as pd
import numpy as np


chat_id = 762047857 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Выполнение двухвыборочного KS-теста (Колмогорова-Смирнова)
    statistic, p_value = ks_2samp(x, y)
    
    # Уровень значимости 0.02
    alpha = 0.02
    
    # Если p-значение меньше alpha, мы отвергаем нулевую гипотезу (различные распределения)
    return p_value < alpha
