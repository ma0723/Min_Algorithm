import sys
sys.stdin = open("2814.txt", "r")
#1 인접행렬
def DFS(idx, cnt):
    global result
    visited[idx] = 1
    # 방문 표시
    if cnt > result:
    # 최장경로 갱신
        result = cnt
    for j in range(1, N+1):
        if not visited[j] and adj[idx][j] == 1:
        # 연결되어 있고
        # 연결된 정점에 방문하지 않은 경우
            DFS(j, cnt + 1)
            # (정점, 경로의 개수)
    visited[idx] = 0
    # 방문 초기화
    # for문을 모두 순회한 후에 초기화를 해야 한다
    # for문 안에 있으면 tc 오답
    # 아래의 정점 i dfs(i)할 때마다 방문배열 초기화하면 for문안 삽입 가능

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 두 개의 자연수 N M(1 ≤ N ≤ 10, 0 ≤ M ≤ 20)
    # N개의 정점과 M개의 간선 가중치가 없는 무방향 그래프

    result = -1
    # 최장 경로의 길이 (경로 상에 등장하는 정점의 개수)

    adj = [[0] * (N+1) for _ in range(N+1)]
    # 인접행렬
    visited = [0]*(N+1)
    # 방문 배열

    for _ in range(M):
        r, c = map(int, input().split())
        # 두 번째 줄부터 M개의 줄에 걸쳐서
        # 그래프의 간선 정보를 나타내는 두 정수 x y(1 ≤ x, y ≤ N)
        # x와 y는 서로 다른 정수이며, 두 정점 사이에 여러 간선이 존재할 수 있다
        adj[r][c] = 1
        adj[c][r] = 1

    for i in range(1, N+1):
    # 각 정점에서 시작
        # visited = [0]*(N+1)
        # 방문배열을 각 정점마다 초기화하면 함수에서 방문초기화 if문 안으로
        DFS(i, 1)

    print("#{} {}".format(tc, result))
    
#2 인접리스트
def dfs(node, N, depth):
    global answer
    if depth > answer:
        answer = depth
    for v in adj[node]:
        if visited[v] == 0:
            visited[v] = 1
            dfs(v, N, depth + 1)
            visited[v] = 0

    for tc in range(1, int(input()) + 1):

        N, M = map(int, input().split())

        adj = [[] for _ in range(N + 1)]

        for _ in range(M):
            a, b = map(int, input().split())
            adj[a].append(b)
            adj[b].append(a)

        answer = 0

        for i in range(1, N + 1):
            visited = [0] * (N + 1)
            dfs(i, N, 0)

        if not answer:
            answer = 1
        print(f"#{tc} {answer}")