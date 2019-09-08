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
<img align="center"  src="https://github.com/blatmand/pathfinding_in_maze/blob/master/recursive_search_algorithm.JPG">

## Maze creation

Create square mazes by randomly asigning each cell a value of
either 0 or 1
Assign a value of 2 to target cell at upper right corner
Two parameters: DIMENSION and ALPHA
DIMENSION: Size of square maze
ALPHA: a measure for the density of walls in the maze

<img align="center"  src="https://github.com/blatmand/pathfinding_in_maze/blob/master/probabilities.png">

## Examples
<img align="left"  src="https://github.com/blatmand/pathfinding_in_maze/blob/master/True2.JPG">
<img align="right"  src="https://github.com/blatmand/pathfinding_in_maze/blob/master/False2.JPG">
<p></p>
<p></p>
<p></p>
<p></p>
<p></p>
## DIMENSION = 6
 