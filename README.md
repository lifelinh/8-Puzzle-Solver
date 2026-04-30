# 8-Puzzle Solver
This project uses state-space search algorithms to solve a sliding 8 tile puzzle. The implemented options include breadth-first, depth-first, greedy, and A* search algorithms.
## Overview
The 8-puzzle is a puzzle that is played on a 3x3 grid, with 8 tiles occupied and one empty space. The objective is to reach a goal state where all tiles are in their correct position, by sliding tiles around. Tiles adjacent to the empty space can be moved by pushing the tile to the empty space. 
## Algorithms
The 8-puzzle can be optimized by completing it with the least amount of movement steps needed. Finding the solution can be done with a state-space search algorithm, which explores a graph of possible board states to find a path from the initial state to the goal state. 

Several different algorithms are available, and each varies in solution accuracy, search speed, or computational efficiency:
<details>
  <summary>Breadth-First Search</summary>
  
  Breadth-first search algorithms explore states level by level and will guarantee that the optimal path is found. However, this method is slow and can be memory-intensive.

  More info: https://en.wikipedia.org/wiki/Breadth-first_search
</details>
<details>
  <summary>Depth-First Search</summary>
  
  Depth-first search algorithms explore as deep as possible, and backtrack if a dead-end state is reached. In this case, the algorithm backtracks if a previously encountered state gets rediscovered by the searcher. This uses less memory, but it rarely will find an optimal solution. Search speed is also highly variable.

  More info: https://en.wikipedia.org/wiki/Depth-first_search
</details>
<details>
  <summary>Greedy Search</summary>
  
  Greedy algorithms will explore the state that seems closest to the goal state. A heuristic must be chosen for the algorithm to measure "closeness" of a state to the goal state. This usually results in fast solutions, but it is not guaranteed to return an optimal path.
</details>
<details>
  <summary>A* Search</summary>
  
  A* Search is a variation of the Greedy algorithm, but it also accounts for the length of the current path. This usually is able to find optimal solutions if the heuristic is accurate.
</details>

## Installation & Usage
This script requires Python to be installed. 

When you've done that, you can download the files by cloning the repository. Cloning the repository requires <a href="https://git-scm.com" target="_blank">Git</a>.

In your terminal:
```bash
git clone https://github.com/lifelinh/8-Puzzle.git
```
Next, start the program using IPython in terminal after navigating to the directory that contains the repository files.
```bash
ipython
%run eight_puzzle.py
```
After that, the solver can be used with the `eight_puzzle()` function, which takes parameters `init_boardstr, algorithm, depth_limit, heuristic`.
<details>
  <summary>init_boardstr</summary>
  
  A string of length 9, which contains digits 0-8. They are the order in which the tiles appear in the initial board state, starting from the upper left and reading across the row. The empty tile is represented by `0`, while the rest of the numbers represent the order of the tile in the solution. This parameter is required.
  
  For example, the below board would be represented as `"345210867"`:
  ```md
  |3|4|5|
  |2|1|_|
  |8|6|7|
```
</details>
<details>
  <summary>algorithm</summary>
  
  A string that contains the name of the search algorithm to solve the puzzle. Accepted inputs are `"BFS"` for breadth-first search, `"DFS"` for depth-first search, `"Greedy"` for greedy search, and `"A*"` for A* search. This parameter is required.
</details>
<details>
  <summary>depth_limit</summary>
  
  An integer that represents how deep search will proceed before backtracking. This parameter is not required; it will default to -1 if left blank, which will be interpreted as having no depth limit.
</details>
<details>
  <summary>heuristic</summary>
  
  A function that represents the heuristic to use. This is required for greedy and A* search algorithms to work properly. Available heuristics are `h1` and `h2`.
  - `h1` measures closeness to the goal state by counting the number of tiles that are in the wrong position. 
  - `h2` measures closeness to the goal state by measuring the Manhattan distance of every tile in their current position to their correct position. 
</details>

### Example
```md
|1|7|4|
|3|8|2|
|6|5|_|
```
To solve the above puzzle using an A* algorithm with heuristic `h2`:
```bash
eight_puzzle("174382650", "A*", heuristic = h2)
```
The result will be a solution that requires 10 moves. You can press `y` to display the steps needed to reach the goal state, or `n` to use the function again.

If a search is taking too long and you would like to terminate it, press `Ctrl` + `C` to interrupt the process. This is likely to happen when using breadth-first search on complex initial states.

### Stopping Usage
To close the program, use `exit` in the terminal.
<hr style="height:2px;border-width:0;color:gray;background-color:gray">

> This repository was originally created for and submitted as a final project for [CAS CS 111](https://www.bu.edu/academics/cas/courses/cas-cs-111/): Introduction to Computer Science 1 at Boston University during the Summer-2 2024 semester. 
