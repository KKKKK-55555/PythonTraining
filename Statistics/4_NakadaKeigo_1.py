import numpy as np


if __name__ == '__main__':
    scores    = [70,80,85,90,75,95,88,92,65,78]
    np_scores = np.array(scores)

    scores_mean = np.mean(np_scores)
    scores_std  = np.std(np_scores)

    scores_h = 50 + ((np_scores - scores_mean)/scores_std)*10

    #np.set_printoptions(precision=3)
    print(scores_h)
