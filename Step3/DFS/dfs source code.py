# DFS는 그래프에서 깊은 부분을 우선 탐색
# 스택 자료구조 이용 (OR 재귀 함수)
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


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, 1, visited)
