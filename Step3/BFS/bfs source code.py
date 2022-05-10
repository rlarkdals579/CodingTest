# 그래프에서 가까운 노드부터 우선적으로 탐색
# 큐 자료구조를 이용
# 특정 조건에서의 최단경로로 자주 사용됨

from collections import deque
graph = [
    [],  # 1번부터 시작이라 비워놓음
    [2, 3, 8],  # 1번노드와 인접한 노드들
    [1, 7],  # 2번노드와 인접한 노드들
    [1, 4, 5],  # 3번노드와 인접한 노드들
    [3, 5],  # 4번노드와 인접한 노드들
    [3, 4],  # 5번노드와 인접한 노드들
    [7],  # 6번노드와 인접한 노드들
    [2, 6, 8],  # 7번노드와 인접한 노드들
    [1, 7]  # 8번노드와 인접한 노드들
]

visited = [False] * 9

def bfs(graph, start, visited):
    queue = deque([start])
    #현재 노드 방문처리
    visited[start] = True
    #큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아서 출력
        v = queue.popleft()
        print(v, end= ' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)
