import sys
sys.stdin = open("5188.txt", "r")

def dfs(start, end, idx, total):
# 모든 경로에 대해 합을 계산한 다음 최소값을 찾아도 된다
    global result
    # 최소값 변경
    if idx == end:
    # 맨 오른쪽 아래 종점에 도착한 경우
        if total < result:
        # 최소값 갱신
            result = total
            return
    if total > result:
    # 가지치기
    # 최소값만 찾으면 되기 때문에 total이 커지는 경우 (자연수의 합이어서 가지치기 가능)
        return
    r = idx[0]
    c = idx[1]
    visited[r][c] = 1
    # 방문 표시
    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc]==0:
        # 경계에서 벗어나지 않는 경우
        # 방문하지 않은 경우
            visited[nr][nc] = 1
            # 방문 표시
            dfs(start, end, [nr, nc], total + lst[nr][nc])
            visited[nr][nc] = 0
            # 방문 초기화
            # 재귀에서 return한 경우

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    # 별로 첫 줄에 가로 세로 칸 수 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 10이하 자연수

    result = 99999999999
    # 지나는 칸에 써진 숫자의 합계

    dr = [1, 0]
    dc = [0, 1]
    # 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다
    
    visited = [[0]*N for _ in range(N)]
    # 방문배열

    start = [0, 0]
    end = [N-1, N-1]
    dfs(start, end, [0, 0], lst[0][0])
    # 맨 왼쪽 위(0, 0)에서 오른쪽 아래(N-1, N-1)까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소 출력

    print("#{} {}".format(tc, result))