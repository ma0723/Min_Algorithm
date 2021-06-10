'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
'''
큐 생성
시작정점을 큐에 삽입
시작정점을 방문했다고 표시

큐가 빌때까지
    큐에서 정점 cur 을 꺼내옴
    정점 cur에 인접한 정점v을 큐에 넣음
    v를 방문했다고 표시
'''
def bfs(n):
# 시작정점
    visited = [0] * (V+1)
    # 방문배열
    # 정점의 갯수만큼 생성(V+1)
    # 0으로 초기화, 방문하면 1로 표시
    q = []
    # 큐생성
    q.append(n)
    # 시작정점 n 삽입
    visited[n] = 1
    # 시작정점 방문 표시

    while q:
    # 큐가 비어있지 않는 동안 반복
        cur = q.pop(0)
        # 큐 front 삭제
        print(cur, end=' ')
        # 현재정점 출력
        for v in range(1,V+1):
        # 주변 정점을 순회하며
            if adj[cur][v] == 1 and visited[v] == 0:
            # 현재정점 cur에 인접하고
            # 아직 방문하지 않은 v면
                q.append(v)
                # 인접 정점 큐 rear 삽입
                visited[v] = 1
                # 방문표시

#그래프의 표현 : 인접행렬, 인접리스트
#탐색기법선정 : dfs bfs
#방문배열
#시작정점을 기준으로 탐색

V,E = map(int,input().split())
edge = list(map(int,input().split()))
adj = [[0 for _ in range(V+1)] for _ in range(V+1)]
# 정점크기 * 정점크기 의 행렬
for i in range(E):
    n1,n2 = edge[i*2],edge[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1

# for row in adj:
#     print(*row)

bfs(1)
# 시작정점을 기준으로 bfs 탐색