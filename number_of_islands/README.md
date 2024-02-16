# Numeber of Islands

Given a binary 2D matrix, find the number of islands where an islands is a group of connected 1s.

## Examples

```
Input: [
    [0, 1, 1],
    [1, 0, 0],
    [0, 0, 1]
]
Expected: 2

Input: [
    [0, 1, 1],
    [1, 0, 0],
    [0, 1, 1],
    [1, 0, 1]
]
Expected: 1

```

## Clarifying Questions

- Should the solution be able to handle an empty matrix? **Yes**
- Is the matrix guarenteed to be a `N x M` grid? **Yes**
- If two `1`s are diagonal from one another, are they considered connected? **Yes**

## Solutions

Use a separate 2D matrix to keep track of visited nodes. Iterate through the graph. When a `1` is found, use DFS to find all connected `1`s. Mark them as visited in the tracking matrix. Increment a counter and continue iterating through the matrix to find unvisited `1`s.

## Follow-Ups

- Why DFS and not BFS? Could you use BFS?