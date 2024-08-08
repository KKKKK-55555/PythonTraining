import numpy as np
import matplotlib.pyplot as plt
import random


def experiment(nExperiment, nTrial, nRoll):

    experiment_results = []

    for iExperiment in range(nExperiment):
        nTrial_ = nTrial*10**iExperiment
        trial_means = trial(nTrial_, nRoll)
        experiment_results.append(trial_means)
    
    return experiment_results


def trial(nTrial, nRoll):
    dice_roll_results_means = []

    for iTrial in range(nTrial):
        dice_roll_results      = roll_dice(nRoll)
        dice_roll_results_mean = np.mean(dice_roll_results)

        dice_roll_results_means.append(dice_roll_results_mean)

    return dice_roll_results_means


def roll_dice(nRoll):
    results = []

    for i in range(nRoll):
        results.append(random.randint(1, 6))
        
    return results


def draw_hists(data_list):

    fig = plt.figure()

    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)
    axs = [ax1, ax2, ax3, ax4]

    for i, data in enumerate(data_list):

        nTrial_ = nTrial*10**i
        data_mean = np.mean(data)
        axs[i].hist(data)
        axs[i].set_title(f'n={nTrial_}(mean={data_mean:.2f})')
    
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':

    nExperiment = 4
    nTrial      = 10
    nRoll       = 5

    experiment_results = experiment(nExperiment, nTrial, nRoll)

    draw_hists(experiment_results)
