import copy
from astar_code import AStar
from search_code import search
from my_functions import create_grid, plot_function, get_walls
DIMENSION = 14
ROW_COUNT = DIMENSION
COLUMN_COUNT = DIMENSION
ALPHA = 0.75

def main():
    """The function main() does the following:
        1. Creates a grid
        2. Test connectivity between the start and end points
        3. If there is connectivity it finds and plots the found path
    """
    grid = create_grid(DIMENSION, ALPHA)
    grid_orig = []
    grid_orig = copy.deepcopy(grid)
    connected = True
    if not search(0, 0, grid):
        print("There is no solution")
        connected = False
    grid = grid_orig

    if connected:
        walls = get_walls(grid, DIMENSION)
        print(walls)
        start = (0, 0)
        end = (DIMENSION-1, DIMENSION-1)
        path = AStar()
        path.init_grid(DIMENSION, DIMENSION, walls, start, end)
        path.solve()
        print(path.get_path())
        moves = path.get_path()
        for i in range(len(moves)):
            grid[moves[i][0]][moves[i][1]] = 3
        plot_function(grid, DIMENSION)
main()
