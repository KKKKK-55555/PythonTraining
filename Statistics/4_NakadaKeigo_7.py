import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_rel


if __name__ == '__main__':

    # initialize data
    before = [150, 140, 180, 170, 140, 100, 200, 160, 120]
    after  = [140, 120, 178, 134, 150, 120 ,150, 140, 100]
    
    # calculate and print mean
    mean_before = np.mean(before)
    mean_after  = np.mean(after)
    print(f'before mean: {mean_before:.3f}')
    print(f'after mean : {mean_after:.3f}')
    
    # calculate and print std
    std_before = np.std(before)
    std_after  = np.std(after)
    print(f'before std: {std_before:.3f}')
    print(f'after std : {std_after:.3f}')
    
    # test
    # t test
    t_stat, p_value = ttest_rel(before, 
                                after,
                                alternative='greater')
    
    print(f't value: {t_stat:.3f}')
    print(f'p value: {p_value}')
