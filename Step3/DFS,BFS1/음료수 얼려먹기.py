import sys

sys.stdin = open("input.txt", "rt")


def dfs(x, y):
    # 주어진 범위 벗어나면 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)  # 좌
        dfs(x, y - 1)  # 하
        dfs(x + 1, y)  # 우
        dfs(x, y + 1)  # 상
        return True
    return False


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
