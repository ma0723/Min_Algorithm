import sys
sys.stdin = open("1861.txt", "r")

def dfs(r, c, start, cnt):
    global num, result
    if result < cnt:
    # 이동하는 방의 최대 개수 갱신
        result = cnt
        # 이동하는 방의 최대 개수
        num = start
        # 처음 출발하는 방 번호
    elif result == cnt:
    # 이동하는 방의 최대 개수가 같다면
        if num > start:
            num = start
            # 처음 출발하는 방 번호가 작은 것 갱신

    for i in range(4):
    # 상하좌우 탐색
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
        # 이동하려는 방이 존재해야 하고
        # 충돌하지 않는 경우
            if room[nr][nc] == room[r][c] + 1:
            # 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다
                dfs(nr, nc, start, cnt + 1)
                # 완전 탐색 (행, 렬, 시작점, 이동하는 방의 개수)
                # 재귀

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    # 1이상 N2 이하의 수 Ai,j가 적혀 있으며, 이 숫자는 모든 방에 대해 서로 다르다.

    visited = [[0]]

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    # 상하좌우 탐색

    result = 0
    # 이동하는 방의 최대 개수(여럿이라면 그 중에서 적힌 수가 가장 작은 것을 출력)
    num = 0
    # 처음 출발하는 방 번호
    
    for i in range(N):
        for j in range(N):
        # 방 list 행 우선 순회하는 for문
            dfs(i, j, room[i][j], 1)
            # 완전 탐색 (행, 렬, 시작점, 이동하는 방의 개수)

    print("#{} {} {}".format(tc, num, result))