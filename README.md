## Pathfinding in 2 dimensional mazes

## Problem description
Goal: deciding whether there is a connection between a
starting and an ending cell in a square 2 dimensional maze.
<img align="right"  src="https://github.com/blatmand/pathfinding_in_maze/blob/master/Example_Grid.png">

Can move in the maze in 4
direction:
Horizontally to the left or
right
Vertically up or down
Cannot move diagonally
Cannot move through walls
(blue)
Cannot move outside the
maze

## Recursive search algorithm

Algorithm uses recursion such that each cell in the maze
delegates the question of connectivity to it’s neighbors (if they
exist) unless the cell itself is the target or has already been
visited
Overall algorithm walks through the maze and avoids walls
and already visited cells.
Pro: algorithm is relatively easy to understand and implement
Returns True or False depending on whether there exists a
path to the target cell
Drawback: does not give the shortest path between the target
and initial cell. For this task there exists e.g. an algorithm
called A*.