'''
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과(재귀)를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
'''
# 입력 부분이 잘못된 것인지 edge도 출력이 안 되서 디버깅이 안 되서 어디가 잘못되었는지 못 찾고 있습니다ㅠㅠ

def bfs(n):
# 시작정점
    visit = [0] * (N + 1)
    # 방문배열
    # 정점의 갯수만큼 생성(N+1)
    # 0으로 초기화, 방문하면 1로 표시
    q = []
    # 큐 생성
    q.append(n)
    # 시작정점 n 삽입
    visit[n] = 1
    # 시작정점 방문 표시
    while q:
    # 큐가 비어있지 않는 동안 반복
        cur = q.pop(0)
        # 큐 front 삭제
        print(cur, end=' ')
        # 현재 정점 가로로 공백 1칸 간격 출력
        for v in range(1,N+1):
        # 주변 정점을 순회하며
            if adj[cur][v] == 1 and visit[v] == 0:
            # 현재정점 cur에 인접하고
            # 아직 방문하지 않은 v면
                q.append(v)
                # 인접 정점 큐 rear 삽입
                visit[v] = 1
                # 방문표시

def dfs(n):
# 시작정점
    print(n, end=' ')
    # 현재 정점 가로로 공백 1칸 간격 출력
    visited[n] = 1
    # 방문 표시
    for i in range(1, N+1):
    # 주변 정점을 순회하며
        if adj[n][i] == 1 and visited[i] == 0:
        # 인접행렬에서 연결된 경우
        # 방문배열이 비어있는 경우
            dfs(i)
            # 재귀

# 인접행렬, 인접리스트
# 탐색기법 : dfs bfs
# 방문배열
# 시작정점을 기준으로 탐색

N, M, V = map(int,input().split())
# 정점의 개수(N), 간선 정보의 개수(M), 시작정점(V)
edge = [list(map(int,input().split())) for _ in range(M)]
# 간선 정보(M개의 줄)
adj = [[0 for _ in range(N+1)] for _ in range(N+1)]
# 정점크기만큼의 인접행렬
for i in range(M):
# 간선 정보의 개수만큼 순회
    n1,n2 = edge[i][0],edge[i][1]
    # 2개의 정점을 한 쌍으로 입력
    # 2차원 배열의 각 행의 인덱스0 인덱스1
    adj[n1][n2] = 1
    adj[n2][n1] = 1
    # 양방향 그래프
visited = [0] * (N + 1)
# 방문배열
# 정점의 갯수만큼 생성(N+1)
# 0으로 초기화, 방문하면 1로 표시

dfs(V)
# 시작정점을 기준으로 dfs 탐색
bfs(V)
# 시작정점을 기준으로 bfs 탐색