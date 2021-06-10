import sys
sys.stdin = open("5102.txt", "r")

def bfs(n, dis, m):
# 시작 정점 n
# 움직인 거리 dis 초기값 1
# 도착 정점 m
    visited = [0]*(V+1)
    # 노드 번호는 1번부터 존재 (V+1)
    # 방문 배열
    dis = [0]*(V+1)
    q = []
    # 큐 생성
    q.append(n)
    # 큐 rear 삽입
    visited[n] = 1
    # 방문 표시
    while q:
        cur = q.pop(0)
        # 큐 front 삭제
        for i in range(1,V+1):
            if adj[cur][i] == 1 and visited[i] == 0:
                q.append(i)
                # 큐 rear 삽입
                visited[i] = 1
                dis[i] = dis[cur] + 1
                # 거리가 1씩 증가하며 이동
                if i == m:
                    return dis[i]
    return 0
    # 도착점과 연결되지 않는다면

T = int(input())
# 첫 줄에 테스트 케이스 개수
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # V개의 노드 개수
    # 방향성이 없는 E개의 간선 정보
    # 다음 줄부터 테스트 케이스의 첫 줄에 V와 E
    edge = [list(map(int, input().split())) for _ in range(E)]
    # 방향성이 없는 E개의 간선 정보
    # 테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 간선의 양쪽 노드 번호가 주어진다.
    S, G = map(int, input().split())
    # E개의 줄 이후에는 출발 노드 S와 도착 노드 G가 주어진다

    adj = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    # 정점크기만큼의 인접행렬

    for i in range(E):
    # 간선 정보의 개수만큼 순회
        n1, n2 = edge[i][0], edge[i][1]
        # 2개의 정점을 한 쌍으로 입력
        # 2차원 배열의 각 행의 인덱스0 인덱스1
        adj[n1][n2] = 1
        adj[n2][n1] = 1
        # 양방향 그래프

    # for i in range(E):
    # # 간선 정보의 개수만큼 순회
    #     a, b = map(int, input().split())
    #     adj[a][b] = 1
    #     adj[b][a] = 1

    print("#{} {}".format(tc, bfs(S, 1, G)))
    # 주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드
    # 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다
    # S와 G가 서로 연결되어 있지 않다면, 0을 출력

def BFS(start, end):
    q = [[start, 0]]
    # 큐 생성 [정점, 거리]
    visited = [0]*(V+1)
    # 방문배열
    visited[start] = 1
    # 방문 표시

    while q:
        v, dis = q.pop(0)
        if v == end:
            return dis
        for i in range(1, V+1):
            if adj[v][i] ==1 and visited[i] == 0:
                q.append([i, dis+1])
                visited[i] = 1
    return 0

def BFS2(start, end):
    q = [start]
    # 큐 생성 [정점]
    visited = [0]*(V+1)
    # 방문배열
    visited[start] = 1
    # 방문 표시

    dis = 0
    while q:
        size = len(q)
        for i in range(size):
            v = q.pop(0)
            # 큐 삭제
            if v == end:
                return dis
                # 거리 반환
            for i in range(1, V + 1):
                if adj[v][i] ==1 and visited[i] == 0:
                    q.append(i)
                    # 큐 삽입
                    visited[i] = 1
        dis += 1
        # 거리 1씩 증가 size for문 순회 후
    return 0
    # 도착점에 도달하지 못한 경우 0 반환