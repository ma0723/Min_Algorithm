import sys
sys.stdin = open("5249.txt","r")

# Prim 재귀 알고리즘
# 10개 중 3개 테스트케이스 통과
# 7개는 최소비용만 고를 떄 서클이 형성되어 있는 경우이므로 이를 고려
# 인덱스를 사용해야 테스트케이스

# 가중치 주변의 인접정점을 검색하고 최소 비용 갱신
# (트리정점/비트리정점) 서로소집합
def MST(idx):
    if idx == V+1:
    # 모든 정점 선택하면
        return
        # 종료
    min_cost = 999999
    min_idx = 0
    for i in range(V+1):
        if adj[idx][i] != 0:
        # 연결되어 있는 경우
            if adj[idx][i] < min_cost:
            # 최소비용 갱신
                min_cost = adj[idx][i]
                min_idx = i
    visited[idx] = min_idx
    # 현재 정점의 방문배열의 값에 연결된 최소 비용 연결 정점 추가
    if visited[min_idx] != idx:
    # 최소 비용 연결 정점이 이미 현재의 정점과 연결되지 않은 경우
        cost_lst.append(min_cost)
        # idx_lst.append(min_idx)
        # 최소 가중치로 연결된 정점 및 가중치 추가
    MST(idx+1)
    # 완전탐색 / 재귀
    # 다음 정점 이동

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 0번부터 V번까지의 노드와 E개의 간선 (0부터 유의)
    adj = [[0]*(V+1) for _ in range(V+1)]
    # 인접행렬
    visited = [-1]*(V+1)
    # 번호가 0번부터 시작해서 -1로 방문배열 초기값 설정
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1][n2] = w
        adj[n2][n1] = w
        # 가중치의 값을 연결 여부와 함께 저장
        # 연결된 경우 가중치
        # 연결되지 않은 경우 0

    cost_lst = []
    # idx_lst = []

    MST(0)
    # 정점 0번부터 MST 생성
    # print(cost_lst)
    # print(idx_lst)

    result = 0
    # 사이클을 제거하고 모든 노드를 포함하는 트리
    # 가중치의 합이 최소가 되도록 만든 경우를 최소신장트리
    # 간선의 가중치를 모두 더해 출력하는 프로그램
    for i in cost_lst:
        result += i

    print("#{} {}".format(tc, result))

#2 Kruskal
'''
1. 가중치 기준 오름차순 정렬 람다 sorted(ratio.items(), key=lambda x: x[2], reverse=True)
2. 가중치가 낮은 것부터 탐색
3. 싸이클이 생기지 않도록 검사
3-1. 서로소집합 생성
3-2. find
4. 정점 연결
4-1. Union
5. 가중치 계산
'''

def FindParent(x):
    if x != parents[x]:
        return FindParent(parents[x])
    return x

def Union(a, b):
    parents[FindParent(b)] = FindParent(a)

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    # 정점, 간선
    
    edge = []
    # 간선 집합
    for _ in range(E):
        edge.append(list(map(int, input().split())))
    edge = sorted(edge, key=lambda x: x[2])
    #1 [2] 세번째 인자 w 가중치에 따라 오름차순 정렬
    #2 가중치를 가장 먼저 놓으면 가중치 기준 오름차순 정렬
    # edge.append((w, u, v))
    # edge.sort()

    parents = [i for i in range(V + 1)]
    # 부모 배열(대표 원소 자기자신)
    # 0번부터 시작해서 (V+1)

    cnt = 0
    # 선택한 정점의 개수
    idx = 0
    # 간선정보 정점 0 idx부터 시작
    result = 0
    # 최소 비용 초기값

    while cnt < V:
    #1 while문 cnt < V 정점의 개수 - 1 개가 될 때까지 반복
    #2 for문 edge 순회 후 if cnt == N=1: break 추가 가능
        n1, n2, w = edge[idx]
        # 시작점, 종점, 가중치
        if FindParent(n1) != FindParent(n2):
        # 대표원소가 다른 경우 
        # 사이클이 생성되지 않도록 서로소 집합
            cnt += 1
            # 선택한 정점의 개수 추가
            result += w
            # 최소비용 추가
            Union(n1, n2)
            # Union 합집합 
        idx += 1
        # 다음 인덱스

    print('#{} {}'.format(tc, result))

# Prim
def extract_min(MST, key, V):
    minV = INF
    u = 0
    for i in range(1, V+1):
        if MST[i] == 0:
            if key[i] < minV:
                u = i
                minV = key[i]
    return u
    # MST 방문하지 않고 최소 비용인 정점 반환

def prim(start, V):
# MST 가중치의 합 리턴
    key = [INF]*(V+1)
    # 가중치 배열
    key[start] = 0
    # 첫 정점 0으로 초기화
    MST = [0]*(V+1)
    # 최소 비용
    pi = [0]*(V+1)
    # 연결되는 정점
    for i in range(V):
    # 모든 정점 순회하는 for문
        u = extract_min(MST, key, V)
        MST[u] = 1
        # 최소 비용 정점 u 방문
        for v in range(start, V+1):
            if MST[v] == 0 and adj[u][v] != 0:
            # u의 인접정점 v를 방문하지 않고 가중치가 있어 연결되는 경우
                if key[v] > adj[u][v]:
                # u에 연결하는 비용이 더 작으면
                    key[v] = adj[u][v]
                    pi[v] = u
                    # v와 u를 연결
    return sum(key[start:])
    # 가중치의 합

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    # 정점, 간선

    INF = 100000

    adj = [[0]*(V+1) for _ in range(V+1)]
    # 인접행렬

    for _ in range(E):
        u, v, w = map(int, input().split())
        adj[u][v] = w
        adj[v][u] = w
        # 가중치의 값을 연결 여부와 함께 저장
        # 연결된 경우 가중치
        # 연결되지 않은 경우 0
    print("#{} {}".format(tc, prim(0, V)))
