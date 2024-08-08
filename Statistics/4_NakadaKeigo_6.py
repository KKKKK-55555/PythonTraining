import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind


if __name__ == '__main__':

    # initialize data
    evaluation_our_product        = [4,5,6,6,7,7,7,8,9,9,9,9]
    evaluation_competitor_product = [1,1,2,2,3,3,3,4,4,4,4,4,5,5,5,6,6,6,6,7]
    
    # calculate and print mean
    mean_evaluation_our_product        = np.mean(evaluation_our_product)
    mean_evaluation_competitor_product = np.mean(evaluation_competitor_product)
    print(f'自社製品の評価平均: {mean_evaluation_our_product:.3f}')
    print(f'他社製品の評価平均: {mean_evaluation_competitor_product:.3f}')
    
    # calculate and print std
    std_evaluation_our_product        = np.std(evaluation_our_product)
    std_evaluation_competitor_product = np.std(evaluation_competitor_product)
    print(f'自社製品の評価標準偏差: {std_evaluation_our_product:.3f}')
    print(f'他社製品の評価標準偏差: {std_evaluation_competitor_product:.3f}')
    
    # 検定する
    # t検定（等分散でないとする場合）
    t_stat, p_value = ttest_ind(evaluation_our_product, 
                                evaluation_competitor_product, 
                                equal_var=True,
                                alternative='greater')
    
    print(f't値: {t_stat:.3f}')
    print(f'p値: {p_value}')
