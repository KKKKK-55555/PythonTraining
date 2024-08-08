import pandas as pd
import math


if __name__ == '__main__':
    p_hat = 0.1
    n = 400

    p_lower = p_hat - 1.96*(math.sqrt((p_hat*(1 - p_hat))/n))
    p_upper = p_hat + 1.96*(math.sqrt((p_hat*(1 - p_hat))/n))

    print(f'{p_lower} <= p <= {p_upper}')

    p_hat = 0.5
    n_min = p_hat*(1 - p_hat)*(2*1.96/0.1)**2

    print(f'n >= {n_min}')