import sys

sys.stdin = open("input.txt", "r")
from collections import deque


def mazeEscape(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 4방향 위치확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 괴물인 경우 무시
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]


graph = []
n, m = map(int, input().split())
for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
"""
왜 이게 상하좌우인가?
2 X 2 배열을 생각해보자
[][] 
[][]

이러한 배열 ARR1 가 있다고 가정할 때, ARR[1][0]의 위치는
[][]
[x][] 이다 

여기서 dx= 를 -1, dy = 0을 해준다면, ARR[0][0]이 된다.
따라서 ARR[0][0]의 위치는

[x][]
[][]
이므로 위로 한칸 이동이 된다. 

"""
print(mazeEscape(0,0))