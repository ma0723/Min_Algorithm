import sys
sys.stdin = open("4871.txt", "r")

# 재귀1 list
def find(S, lst):
    lst.append(S)
    # 경로의 정점들을 담을 빈 리스트 초기값
    visited[S] = 1
    # 방문 배열 표시
    for i in range(V+1):
        if adj[S][i] == 1 and visited[i] == 0:
        # 인접행렬에서 연결된 경우
        # 방문배열이 비어있는 경우
            find(i, lst)
            # 재귀

T = int(input())
# 첫 줄에 테스트 케이스 개수 T
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 다음 줄부터 테스트 케이스의 첫 줄에 V와 E
    edge = [list(map(int, input().split())) for _ in range(E)]
    # 둘째 줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보
    S, G = map(int, input().split())
    # E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G

    adj = [[0]*(V+1) for _ in range(V+1)]
    # 인접행렬
    visited = [0]*(V+1)
    # 방문배열
    # 노드번호는 1번부터 존재(V+1)

    for i in edge:
        adj[i[0]][i[1]] = 1
        # 방향성 그래프
        # 인접행렬의 한 부분에만 1을 표기

    lst = []
    # 빈 리스트 초기값
    find(S, lst)

    if G in lst:
        print("#{} {}".format(tc, 1))
    else:
        print("#{} {}".format(tc, 0))
    # 특정한 두 개의 노드에 경로가 존재하는지 확인
    # 두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력

# # 재귀2 dictionary
# def dfs(n):
# # 현재 정점 n
#     if n == end:
#         return 1
#     else:
#         for i in adj[n]:
#         # 인접 행렬 dictionary의 value를 순회하는 for문
#             if visited[i] == 0:
#             # 방문하지 않았다면
#                 visited[i] = 1
#                 # 방문 표시
#             if dfs(i) == 1:
#             # 도착했다면
#                 return 1
#                 # 1 return
#         return 0
#         # 도착하지 않았다면
#         # 0 return
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     # 정점 개수, 간선 정보 개수
#     visited = {i:0 for i in range(1, V+1)}
#     # 방문배열
#     adj = {i:[] for i in range(1, V+1)}
#     # 인접행렬
#     # dictionary or list 입력 모두 가능
#     for i in range(E):
#         u, v = map(int, input().split())
#         # 간선 정보
#         adj[u].append(v)
#         # dictionary key값의 value에 추가
#     start, end = map(int, input().split())
#     print("#{} {}".format(tc, dfs(start)))

# # stack
# def dfs(n, end):
#     visited = [0]*(V+1)
#     # 방문 배열 초기값
#     stack = []
#     # stack 초기값
#     stack.append(n)
#     # stack push
#     visited[n] = 1
#     # 방문 표시
#     while stack:
#     # stack이 존재하면
#         cur = stack.pop()
#         # top pop
#         if cur == end:
#         # 도착점이면
#             return 1
#         for i in range(1, V+1):
#             if adj[cur][i] == 1 and visited[i] == 0:
#             # 인접행렬에 존재하고(연결)
#             # 방문하지 않았다면
#                 stack.append(i)
#                 # stack push
#                 visited[i] = 1
#                 # 방문 표시
#     return 0
#     # stack이 빈 이후에도
#     # 도착점이 아니라면

# T = int(input())
# for tc i rnage(1, T+1):
#     V, E = map(int, input().split())
#     # 정점의 개수, 간선의 개수
#     adj = [[0 for i in range(V+1)] for _ in range(V+1)]
#     for i in range(E):
#     # 간선의 개수만큼 순회
#         u, v = map(int, input().split())
#         # 간선 정보 시작점과 끝점
#         adj[u][v] = 1
#         # 방향성 그래프 일방향만 1
#     S, G = map(int, input().split())
#     # 시작점과 도착점
#     result = dfs(S, G)
#     print("#{} {}".format(tc, result))