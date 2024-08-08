import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def draw_hist():
    nExperiment   = 4
    average       = 70
    std_deviation = 10
    sample_size   = 10

    fig = plt.figure()

    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)
    axs = [ax1, ax2, ax3, ax4]

    #y_norm = norm.pdf()

    for iExperiment in range(nExperiment):
        sample_size = sample_size*10**iExperiment

        data = np.random.normal(loc=average, scale=std_deviation, size=sample_size)
        
        data_mean = np.mean(data)
        print(f'n={sample_size}: {data_mean}')
        
        axs[iExperiment].hist(data)
        axs[iExperiment].set_title(f'n={sample_size}(mean={data_mean:.2f})')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    draw_hist()
