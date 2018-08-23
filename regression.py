import numpy as np
from data_preprocessing import convert_datatype


def linear_regression(x,y):
    """
    Simple linear regression ,
    x is the input
    y is the output
    """
    x = convert_datatype(x,"array")
    y = convert_datatype(y, "array")
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    num = 0.0
    denom = 0.0
    for i in range(len(x)):
        num += (x[i] - x_mean) * (y[i] - y_mean)
        denom += (x[i] - x_mean)**2
    m = num / denom
    c = y_mean - (m * x_mean)
    return m,c

def logistic_regression(x, y):
    pass

def multi_linear_regression(x, y):
    pass

def multi_logistic_regression(x, y):
    pass
