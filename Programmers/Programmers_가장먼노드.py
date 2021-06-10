# 시간 초과의 경우 인접행렬보다 인접리스트로 초기값 구성

from collections import deque
# stack (append, pop)
# queue (append, pop, popleft, appendleft, extend, extendleft)
# insert(index, value), remove(value) (같은값일 때에는 왼쪽부터)

def solution(n, edge):
# 노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex
    answer = 0
    # 가장 멀리 떨어진 노드의 갯수
    adj = [[0]*(n+1) for _ in range(n+1)]
    # 각 노드는 1부터 n까지 번호 (인덱스 일치를 위해 n+1)
    for i in edge:
    # 간선 2차원 배열 순회
        r = i[0]
        c = i[1]
        adj[r][c] = 1
        adj[c][r] = 1
        # 간선은 양방향 그래프
    visited = [-1]*(n+1)
    # 방문 거리 배열(거리를 위해 -1로 초기값 설정)
    BFS(1, visited, adj, n)
    # BFS(시작점, 방문배열, 인접행렬, 노드의 개수)
    for distance in visited:
    # 방문 거리 배열 순회
        if distance == max(visited):
        # 거리 최대값과 같을 때
            answer += 1
            # 가장 멀리 떨어진 노드의 갯수
    return answer

def BFS(start, visited, adj, n):
# 1번 노드에서 가장 멀리 떨어진 노드의 갯수
# 1번부터 각 노드에 대한 최단 거리
    dis = 0
    # 초기 거리값(자기 자신은 0)
    q = deque([[start, dis]])
    # 큐 2차원 배열로 삽입 [[시작점, 거리]]
    while q:
    # 큐의 내용이 사라지면
        value = q.popleft()
        # front 삭제
        v = value[0]
        distance = value[1]
        # 정점, 거리
        if visited[v] == -1:
        # 정점을 방문하지 않았다면
            visited[v] = distance
            # 방문 표시를 거리값으로 삽입
            distance += 1
            # 거리가 1씩 증가
            for e in range(1, n+1):
            # 인접행렬 순회
                if adj[v][e] and visited[e] == -1:
                # 인접정점 연결 + 인접정점을 방문하지 않은 경우
                    q.append([e, distance])
                    # 큐 [정점, 거리] rear 삽입

# 시간 초과의 경우 인접행렬보다 인접리스트로 초기값 구성

from collections import deque
# stack (append, pop)
# queue (append, pop, popleft, appendleft, extend, extendleft)
# insert(index, value), remove(value) (같은값일 때에는 왼쪽부터)

def solution(n, edge):
# 노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex
    answer = 0
    # 가장 멀리 떨어진 노드의 갯수
    adj = [[] for _ in range(n + 1)]
    # adj = [[] * (n+1) ] 리스트가 비어있어서 인덱스 오류
    # 각 노드는 1부터 n까지 번호 (인덱스 일치를 위해 n+1)
    # 인접행렬(2차원 배열) 시간 초과 < 인접 리스트(1차원 배열)
    for i in edge:
    # 간선 2차원 배열 순회
        r = i[0]
        c = i[1]
        adj[r].append(c)
        adj[c].append(r)
        # adj[r][c] = 1
        # adj[c][r] = 1
        # 간선은 양방향 그래프
    visited = [-1]*(n+1)
    # 방문 거리 배열(거리를 위해 -1로 초기값 설정)
    BFS(1, visited, adj, n)
    # BFS(시작점, 방문배열, 인접행렬, 노드의 개수)
    for distance in visited:
    # 방문 거리 배열 순회
        if distance == max(visited):
        # 거리 최대값과 같을 때
            answer += 1
            # 가장 멀리 떨어진 노드의 갯수
    return answer

def BFS(start, visited, adj, n):
# 1번 노드에서 가장 멀리 떨어진 노드의 갯수
# 1번부터 각 노드에 대한 최단 거리
    dis = 0
    # 초기 거리값(자기 자신은 0)
    q = deque([[start, dis]])
    # 큐 2차원 배열로 삽입 [[시작점, 거리]]
    while q:
    # 큐의 내용이 사라지면
        value = q.popleft()
        # front 삭제
        v = value[0]
        distance = value[1]
        # 정점, 거리
        if visited[v] == -1:
        # 정점을 방문하지 않았다면
            visited[v] = distance
            # 방문 표시를 거리값으로 삽입
            distance += 1
            # 거리가 1씩 증가
            for e in adj[v]:
            # 인접리스트 순회
            # 인접행렬 순회
                # if adj[v][e] and visited[e] == -1:
                # 인접정점 연결 + 인접정점을 방문하지 않은 경우
                q.append([e, distance])
                # 큐 [정점, 거리] rear 삽입