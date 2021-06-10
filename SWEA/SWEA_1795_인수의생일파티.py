import sys
sys.stdin = open("1795.txt","r")

def dijkstra(N, X, adj, dis):
# 최단거리 다익스트라 알고리즘
# (집의 수, 목표 집의 번호, 비용그래프, 거리배열)
    for i in range(N+1):
    # X번의 집으로부터 모든 정점으로까지의 비용값 할당
        dis[i] = adj[X][i]
        # 거리비용값 할당
    visited = [0]*(N+1)
    # 방문 배열
    for _ in range(N-1):
    # 모든 정점 순회(X번 집 제외 N-1개)
        min_idx = 0
        for u in range(1, N+1):
        # 1번부터 N번까지 마을 순회
            if not visited[u] and dis[u] < dis[min_idx]:
            # 방문하지 않고 (visited[u])
            # 최소거리비용 (dis[u] < dis[min_idx])
                min_idx = u
                # 최단 거리 정점
        visited[min_idx] = 1
        # 최단 거리 정점 방문 표시
        # 최단 거리 비용 결정
        for v in range(1, N+1):
        # 최간 거리 정점의 인접 정점 순회
        # 1번부터 N번까지 마을 순회
            if min_idx != v and adj[min_idx][v] < INF:
            # 최단거리 정점과 같은 정점이 아닌 (min_idx != v)
            # 인접정점 (adj[min_idx][i] < INF)
                dis[v] = min(dis[v], dis[min_idx] + adj[min_idx][v])
                # 최단거리비용 결정
                # dis[v]의 기본값은 INF
                # 최단거리비용 + 최단거리정점과 인접정점의 거리비용 값으로 갱신
                # 갱신 후 최소값을 찾기 위해 모든 정점을 순회하는 상단의 for문으로 이동
    
T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    # 세 정수 N,M,X(1 ≤ X ≤ N ≤ 1,000, 1 ≤ M ≤ 10,000)
    # 1번에서 N번까지의 번호를 붙일 때, 인수의 집은 X번 집

    INF = 10000000
    adj1 = [[INF]*(N+1) for _ in range(N+1)]
    # 진출 기준
    adj2 = [[INF]*(N+1) for _ in range(N+1)]
    # 진입 기준

    for i in range(N+1):
    # 출발지와 도착지가 같은 경우
        adj1[i][i] = 0
        adj2[i][i] = 0

    for _ in range(M):
    # 출발지와 도착지가 다른 경우
        x, y, c = map(int, input().split())
        #  M개의 각 줄에는 세 정수 x, y, c (1 ≤ x, y ＜ N, 1 ≤ c ≤ 100)가 공백
        adj1[x][y] = c
        adj2[y][x] = c

    dis1 = [INF]*(N+1)
    dis2 = [INF]*(N+1)
    # 거리배열

    dijkstra(N, X, adj1, dis1)
    dijkstra(N, X, adj2, dis2)
    # 각 사람들은 자신의 집에서 X번 집으로 오고 가기 위해 최단 시간으로 이동

    result = 0
    # 진입 진출 시간의 합 최대값 초기값
    # X번 집으로 오고 가는데 드는 시간 중에서 가장 오래 걸리는 집은 어느 정도 걸리는지 구하는 프로그램
    for i in range(1, N+1):
        if dis1[i] + dis2[i] > result:
            result = dis1[i] + dis2[i]

    print('#{} {}'.format(tc, result))