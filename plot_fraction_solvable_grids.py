import matplotlib.pyplot as plt
from my_functions import compute_probability
DIMENSION = 10

def main():
    """
    plots the results of the computation of
    the solvability fraction for different values of alpha
    """
    [x_65, y_65] = compute_probability(DIMENSION, 0.65)
    [x_70, y_70] = compute_probability(DIMENSION, 0.70)
    [x_75, y_75] = compute_probability(DIMENSION, 0.75)
    [x_80, y_80] = compute_probability(DIMENSION, 0.80)
    [x_90, y_90] = compute_probability(DIMENSION, 0.90)

    f, axes = plt.subplots(1)
    axes.scatter(x_65, y_65, s=10, c='b', marker="o", label='ALPHA = 0.65')
    axes.scatter(x_70, y_70, s=10, c='y', marker="o", label='ALPHA = 0.70')
    axes.scatter(x_75, y_75, s=10, c='r', marker="o", label='ALPHA = 0.75')
    axes.scatter(x_80, y_80, s=10, c='g', marker="o", label='ALPHA = 0.80')
    axes.scatter(x_90, y_90, s=10, c='m', marker="o", label='ALPHA = 0.90')
    plt.legend(loc='upper left', prop={'size':25}, bbox_to_anchor=(1, 1))
    axes.set_xlabel('number of created mazes')
    axes.set_ylabel('fraction of solvable mazes')
    axes.set_ylim(ymin=0)
    axes.set_xlim(left=0)
    plt.savefig('probabilities.png', bbox_inches='tight')
    plt.show()
main()
