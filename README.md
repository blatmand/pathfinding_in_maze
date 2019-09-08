## Pathfinding in 2 dimensional mazes

## Problem description
Goal: deciding whether there is a connection between a
starting and an ending cell in a square 2 dimensional maze.
<img align="right"  src="https://github.com/blatmand/pathfinding_in_maze/blob/master/Example_Grid.png">

* Can move in the maze in 4
direction:
* Horizontally to the left or
right
* Vertically up or down
* Cannot move diagonally
* Cannot move through walls
(blue)
* Cannot move outside the maze

## Recursive search algorithm

* Algorithm uses recursion such that each cell in the maze
delegates the question of connectivity to it’s neighbors (if they
exist) unless the cell itself is the target or has already been
visited
* Overall algorithm walks through the maze and avoids walls
and already visited cells.
* Pro: algorithm is relatively easy to understand and implement
* Returns True or False depending on whether there exists a
path to the target cell
* Drawback: does not give the shortest path between the target
and initial cell. For this task there exists e.g. an algorithm
called A*.
<img align="center"  src="https://github.com/blatmand/pathfinding_in_maze/blob/master/recursive_search_algorithm.JPG">

## Maze creation

* Create square mazes by randomly asigning each cell a value of
either 0 or 1
* Assign a value of 2 to target cell at upper right corner
* Two parameters: DIMENSION and ALPHA
* DIMENSION: Size of square maze
* ALPHA: a measure for the density of walls in the maze

<img align="center"  src="https://github.com/blatmand/pathfinding_in_maze/blob/master/probabilities.png">

## Examples
<img align="left"  src="https://github.com/blatmand/pathfinding_in_maze/blob/master/True2.JPG">
<img align="right"  src="https://github.com/blatmand/pathfinding_in_maze/blob/master/False2.JPG">

<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>

## &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; DIMENSION = 6
<img align="left"  src="https://github.com/blatmand/pathfinding_in_maze/blob/master/True.JPG">
<img align="right"  src="https://github.com/blatmand/pathfinding_in_maze/blob/master/False.JPG">

<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>

## &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; DIMENSION = 14

## Examples of pathfinding using A* algorithm

<img align="center"  src="https://github.com/blatmand/pathfinding_in_maze/blob/master/Plot1.png">

## &emsp;&emsp;&emsp;&emsp;&emsp;&nbsp; DIMENSION = 6

<img align="center"  src="https://github.com/blatmand/pathfinding_in_maze/blob/master/Plot2.png">

## &emsp;&emsp;&emsp;&emsp;&emsp;&nbsp; DIMENSION = 4

## Further example

<img align="center" width = "864"   src="https://github.com/blatmand/pathfinding_in_maze/blob/master/Plot3.png">

## &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp; DIMENSION = 30

### Create maze of given dimension
### Run recursive search to determine solvability
### If solvable−→run A* to find the path

## Summary and results

### * Can generate square mazes with randomly distributed
### locations of walls
### * Dimension of maze and density of walls adjustable
### * Recursive search algorithm decides wthether there is a
### solution to the maze
### * A* algorithm can plot the optimal path if it exists

## Bibliography

### Recursive search algorithm and A* algorithm
### https://www.laurentluce.com/posts/solving-mazes-using-python-simple-recursivity-and-a-search/
### A* algorithm on GitHub:
### https://github.com/laurentluce/python-algorithms/blob/master/algorithms/a_star_path_finding.py
