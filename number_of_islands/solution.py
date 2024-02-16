def is_safe(i, j, visited):
    in_row_bounds = i < len(visited) and i >= 0
    in_col_counds = j < len(visited[0]) and j >= 0
    return in_row_bounds and in_col_counds and not visited[i][j]


def DFS(i, j, visited, graph):
    # directions -1, 0, 1
    row_modifier = [-1, -1, -1, 0, 1, 1, 1, 0]
    col_modifier = [-1, 0, 1, 1, 1, 0, -1, -1]

    visited[i][j] = True

    for x, y in zip(row_modifier, col_modifier):
        if is_safe(i + x, j + y, visited) and graph[i + x][j + y] == 1:
            DFS(i + x, j + y, visited, graph)


def countIslands(graph) -> int:
    row = len(graph)
    col = len(graph[0])

    visited = [
        [False for _ in range(col)] for _ in range(row)
    ]

    island_count = 0

    for i in range(row):
        for j in range(col):
            if graph[i][j] == 1 and visited[i][j] == False:
                DFS(i, j, visited, graph)
                island_count += 1
                print(i, j)

    return island_count


if __name__ == "__main__":
    print(countIslands([[1,1],[1,1],[0,0],[1,0]]))