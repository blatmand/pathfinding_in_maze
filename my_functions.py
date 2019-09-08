import random
import copy
from matplotlib import colors
from matplotlib import pyplot as plt
import numpy as np
from search_code import search
def create_grid(dimension, alpha):
    """ Creates a square grid with width and height of size dimension
        The parameter alpha is a measure for the density of walls in the grid
        The possible values for the grid cells are
        0 (not a wall), 1 (a wall), 2 (end cell)
        The start cell is the (0,0) cell and is assigned a value of 0
        The end cell is the upper right cell and is assigned a value of 2
    """
    row_count = dimension
    column_count = dimension
    grid = []
    for row in range(row_count):
        grid.append([])
        for column in range(column_count):
            if random.random() > alpha:
                cell_type = 1
            else:
                cell_type = 0
            grid[row].append(cell_type)
    grid[dimension-1][dimension-1] = 2
    grid[0][0] = 0
    return grid

def plot_function(data, dimension):
    """ plots the path found by the astar algorithm
        data is the input grid
        dimension is the size of the square grid
    """
    grid_plt = []

    grid_plt = copy.deepcopy(data)
    for i in range(dimension):
        for j in range(dimension):
            grid_plt[i][j] = data[j][i]
    cmap = colors.ListedColormap(['red', 'blue', 'green'])
    bounds = [0, 1, 2, 3]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    fig, axes = plt.subplots()
    extent = [0, dimension, dimension, 0]
    axes.imshow(grid_plt, cmap=cmap, norm=norm, extent=extent)

    # draw gridlines
    axes.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
    axes.set_xticks(np.arange(0, dimension+1, 1.0))
    axes.set_yticks(np.arange(0, dimension+1, 1.0))
    #fig.suptitle(a, fontsize=12)
    plt.gca().invert_yaxis()
    #plt.title('my title')
    #plt.savefig('test', bbox_inches='tight')
    #plt.savefig('Plot3')
    plt.show()
def get_walls(grid, dimension):
    """ fills the walls array from a given grid
    """
    row_count = dimension
    column_count = dimension
    walls = []
    for i in range(row_count):
        for j in range(column_count):
            if grid[i][j] == 1:
                walls.append((i, j))
    return walls
def compute_probability(dimension, alpha):
    """ computes the fraction of solvable mazes out of randomly created mazes with
        a given dimension and parameter alpha
    """
    probabilities = []
    numbers = []
    for i in range(1, 15):
        counter = 0
        total_number = 10000*i
        for i in range(total_number):
            grid = create_grid(dimension, alpha)
            connected = search(0, 0, grid)
            if connected:
                counter = counter +1
        probability = counter /total_number
        print("the probability to find a path is ", \
        probability, "where the total_number is ", total_number)
        probabilities.append(probability)
        numbers.append(total_number)
    print(probabilities)
    print(numbers)
    retvec = [numbers, probabilities]
    return retvec
