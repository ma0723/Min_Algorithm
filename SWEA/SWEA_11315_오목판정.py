import sys
sys.stdin = open("11315.txt", "r")

def index(r, c, dir):
    idx = []
    if lst[r][c] == 'o':
        idx.append(r)
    while True:
        nr = r + dr[dir]
        nc = c + dc[dir]
        # 좌하측 대각선
        # 우하측 대각선
        if 0 <= nr < N and 0 <= nc < N:
        # 벽에 부딪히지 않을 경우
            if lst[nr][nc] == 'o':
                idx.append(nr)
                r = nr
                c = nc
        if r == N-1:
        # 마지막 행에 도달한 경우
            break
            # while문 종료
    return idx

def index2(r, c, dir):
    idx = []
    if lst[r][c] == 'o':
        idx.append(r)
    while True:
        nr = r + dr[dir]
        nc = c + dc[dir]
        # 좌하측 대각선
        # 우하측 대각선
        if 0 <= nr < N and 0 <= nc < N:
        # 벽에 부딪히지 않을 경우
            if lst[nr][nc] == 'o':
                idx.append(nr)
                r = nr
                c = nc
        if c == N-1:
        # 마지막 열에 도달한 경우
            break
            # while문 종료
    return idx

def omok(idx):
    result = 0
    for k in range(len(idx)-4):
    # 다섯 개 '연속' '이상' 유의
        cnt = 0
        for l in range(5):
            if idx[k + l] == idx[k] + l:
                cnt += 1
                # '연속'한 부분의 개수
            else:
                break
        if cnt == 5:
        # '이상'인 부분의 개수
            result += 1
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 첫 번째 줄에는 하나의 정수 N(5 ≤ N ≤ 20)이
    lst = [list(input()) for _ in range(N)]
    # N X N 크기의 판
    # N개의 줄의 각 줄에는 길이 N인 문자열
    # 각 문자는 ‘o’는 돌이 있는 칸을 의미하고, ‘.’는 돌이 없는 칸

    result = 0
    # 돌이 다섯개 '이상' '연속' 부분의 개수
    # 이상 cnt >= 5
    # 연속

    for i in range(N):
    # 행 고정 열 변화
    # 가로 탐색
        idx = []
        # 돌이 있는 위치 인덱스를 담을 빈 리스트 초기값
        for j in range(N):
            if lst[i][j] != 'o':
                break
            else:
                idx.append(j)
        result += omok(idx)

    for i in range(N):
    # 열 고정 행 변화
    # 세로 탐색
        idx = []
        # 돌이 있는 위치 인덱스를 담을 빈 리스트 초기값
        for j in range(N):
            if lst[j][i] != 'o':
                break
            else:
                idx.append(j)
        result += omok(idx)

    dr = [1, 1]
    # 하
    dc = [1, -1]
    # 우좌

    for c in range(0, N-4):
    # (0, N-5)...(0,0)에서 시작하는 모든 대각선 확인(행 고정 열 변화)
    # while 종료 조건 열이 N-1
        r = 0
        # 우하측
        idx = index2(r, c, 0)
        result += omok(idx)

    for r in range(1, N-4):
    # (1,0) (2,0) (3,0) ... (N-5, 0)에서 시작하는 모든 대각선 확인(열 고정 행 변화)
    # while 종료 조건 행이 N-1
        c = 0
        # 우하측
        idx = index(r, c, 0)
        result += omok(idx)

    for c in range(4, N):
    # (0, 4)...(0, N-1)에서 시작하는 모든 대각선 확인(행 고정 열 변화)
    # while 종료 조건 열이 N-1
        r = 0
        # 좌하측
        idx = index2(r, c, 1)
        result += omok(idx)

    for r in range(1, N-4):
    # (1, N-1) (2, N-1) ... (N-5, N-1)에서 시작하는 모든 대각선 확인(열 고정 행 변화)
    # while 종료 조건 행이 N-1
        c = N-1
        idx = index(r, c, 1)
        result += omok(idx)

    if result == 0:
        print("#{} {}".format(tc, 'NO'))
        # 돌이 가로, 세로, 대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분이 있는지 없는지 판정
    else:
        print("#{} {}".format(tc, 'YES'))
        # 돌이 다섯 개 이상 연속한 부분이 있으면 “YES”를, 아니면 “NO”를 출력