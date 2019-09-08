## Pathfinding in 2 dimensional mazes

```
Daniel Blatman
```
```
Data Science Project presentation
```
```
SPICED Academy, Berlin, 20 August, 2019
```

## Outline

(^1) Introduction
(^2) Recursive search algorithm
(^3) A* algorithm
4 Summary


## Introduction

```
Problem description
Goal: deciding whether there is a connection between a
starting and an ending cell in a square 2 dimensional maze.
```
```
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
```

## Recursive search algorithm

```
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
```

## Recursive search algorithm


Maze creation

```
Create square mazes by randomly asigning each cell a value of
either 0 or 1
Assign a value of 2 to target cell at upper right corner
Two parameters: DIMENSION and ALPHA
DIMENSION: Size of square maze
ALPHA: a measure for the density of walls in the maze
```

## Examples

```
DIMENSION = 6
```
```
DIMENSION = 14
```

## Examples of pathfinding using A* algorithm

```
DIMENSION = 6
```
```
DIMENSION = 4
```

## Further example

```
DIMENSION = 30
```

## Demonstration

```
Create maze of given dimension
Run recursive search to determine solvability
If solvable−→run A* to find the path
```

## Summary and results

```
Can generate square mazes with randomly distributed
locations of walls
Dimension of maze and density of walls adjustable
Recursive search algorithm decides wthether there is a
solution to the maze
A* algorithm can plot the optimal path if it exists
```

## Bibliography

```
Further Reading
For those interested in learning more about it: Recursive
search algorithm and A* algorithm
https://www.laurentluce.com/posts/......
solving-mazes-using-python-simple-recursivity...
...-and-a-search/
A* algorithm on GitHub:
https://github.com/laurentluce/python-algorithms/
blob/master/algorithms/a_star_path_finding.py
```
# Thank you for your attention

## Do you have any questions?


