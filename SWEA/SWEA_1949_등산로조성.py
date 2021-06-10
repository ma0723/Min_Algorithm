import sys
sys.stdin =  open("1949.txt", "r")

def dfs(r, c, cnt, N, K):
    global result
    if result < cnt + 1:
        result = cnt + 1
        # 5번 이동하는 경우 등산로는 최종 도착지 경로까지 6(5+1)
    visited[r][c] = 1
    # 방문표시
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    for i in range(4):
    # 높이가 같은 곳 혹은 낮은 지형이나, 대각선 방향의 연결은 불가능 (4방 탐색)
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
        # 배열 안에 존재하는 경우
            if visited[nr][nc]==0:
            # 방문하지 않은 경우
                if mt[nr][nc] < mt[r][c]:
                # 공사하지 않는 경우
                    dfs(nr, nc, cnt+1, N, K)
                    # 경로 1씩 추가
                elif mt[nr][nc] -K < mt[r][c]:
                # 공사하는 경우 (최대 깊이 K 1번 공사)
                    origin = mt[nr][nc]
                    mt[nr][nc] = mt[r][c] - 1
                    # 가장 긴 경로를 위해 이전 높이보다 1만큼만 작게 높이 공사
                    # 지형은 정수 단위로만 깎을 수 있다.
                    # 최대 공사 가능 깊이 K (1 ≤ K ≤ 5)
                    dfs(nr, nc, cnt + 1, N, 0)
                    # 공사한 이후에는 K=0 초기화
                    mt[nr][nc] = origin
                    # 다른 경로 검색하는 경우를 위해 공사한 이후에는 값 복귀
    visited[r][c] = 0
    # 다른 경로 검색하는 경우를 위해 방문 초기화

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    mt = [list(map(int, input().split())) for _ in range(N)]
    # 등산로를 만들기 위한 부지는 N * N 크기
    # 지도의 한 변의 길이 N은 3 이상 8 이하의 정수이다. (3 ≤ N ≤ 8)
    # 각 숫자는 지형의 높이 (1 이상 20 이하의 정수)

    my_max = 0
    my_index = []
    for i in range(N):
        for j in range(N):
            if mt[i][j] > my_max:
                my_max = mt[i][j]

    for i in range(N):
        for j in range(N):
            if mt[i][j] == my_max:
                my_index.append([i, j])
    # 가장 높은 봉우리에서 시작
    # 지도에서 가장 높은 봉우리는 최대 5개

    visited = [[0]*N for _ in range(N)]
    # 방문배열
    result = 0
    # 가장 긴 등산로를 찾아 그 길이를 출력 (경로의 개수 + 1)

    for i in range(len(my_index)):
        dfs(my_index[i][0], my_index[i][1], 0, N, K)
        # dfs (행, 열, 등산로 길이, 배열 크기, 최대 높이)

    print("#{} {}".format(tc, result))






