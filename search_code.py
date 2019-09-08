def search(x, y, grid):
    """ Tests for connecivity between cell (x,y) and the end cell
        in a given grid
    """
    if grid[x][y] == 2:
        return True
    if grid[x][y] == 1:
        return False
    if grid[x][y] == 3:
        return False
    # mark as visited
    grid[x][y] = 3

    # explore neighbors clockwise starting by the one on the right
    if (((x < len(grid)-1) and search(x+1, y, grid))
            or (y > 0 and search(x, y-1, grid))
            or (x > 0 and search(x-1, y, grid))
            or (y < len(grid)-1 and search(x, y+1, grid))):
        return True

    return False
