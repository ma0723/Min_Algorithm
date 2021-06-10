import sys
sys.stdin  = open("4875.txt", "r")

# 가장 좌상단에 있는 칸을 (0, 0)의 기준으로 하여, 가로방향을 x 방향, 세로방향을 y 방향

def bfs(x, y):
    global result
    # 기본값 0에서 변경하기 위해 global
    q = []
    # 큐 생성
    q.append((x, y))
    # 큐 rear tuple 행렬 인덱스 삽입
    visited[x][y] = 1
    # 방문표시
    while q:
    # 큐가 존재하는 동안
        r, c = q.pop(0)
        # 큐 front 삭제
        for i in range(4):
        # 상하좌우
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 16 and 0 <= nc < 16 and lst[nr][nc]!=1 and visited[nr][nc]==0:
            # 미로를 벗어나지 않고
            # 벽이 아닌 경우
            # 방문하지 않은 경우
                q.append((nr, nc))
                # 큐 rear tuple 행렬 인덱스 삽입
                visited[nr][nc] = 1
                # 방문 표시
                if lst[nr][nc] == 3:
                # 도착지인 경우
                    result = 1
                    return

T = 10
for tc  in range(1, T+1):
    N = int(input())
    lst = [[int(i) for i in input()] for _ in range(16)]
    # 16*16 행렬의 형태로 만들어진 미로

    start = []
    for i in range(16):
        for j in range(16):
            if lst[i][j] == 2:
                start.append(i)
                start.append(j)

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    # 상하좌우

    visited = [[0]*16 for _ in range(16)]
    # 방문배열

    result = 0
    # 기본값 0
    bfs(start[0], start[1])
    # 시작점 행렬 인덱스

    print("#{} {}".format(tc, result))
    # 공백 문자 후 도달 가능 여부를 1 또는 0으로 표시

# DFS(재귀)
# def DFS(r, c):
#     global result
#     # 기본값 0에서 변경하기 위해 global
#     if lst[r][c] == 3:
#         result = 1
#         return
#     lst[r][c] = 1
#     # 방문 표시
#     for i in range(4):
#     # 상하좌우
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < 16 and 0 <= nc < 16 and lst[nr][nc] != 1 and visited[nr][nc] == 0:
#         # 미로를 벗어나지 않고
#         # 벽이 아닌 경우
#         # 방문하지 않은 경우
#             DFS(nr, nc)
#             # 재귀
        