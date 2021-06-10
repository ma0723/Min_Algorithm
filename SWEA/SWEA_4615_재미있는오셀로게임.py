import sys
sys.stdin = open("4615.txt", "r")

def trans(r, c, origincolor, transcolor):
    for j in range(8):
    # 이동 방향
        nr = r + dr[j]
        nc = c + dc[j]
        change_lst = []
        # 사이의 변경할 상대편의 돌 인덱스 저장 리스트
        need = False
        # 자신의 돌이 이동 방향 속에 존재하는 경우 변경 필요
        nr = r + dr[j]
        nc = c + dc[j]
        while 0 <= nr < N and 0 <= nc < N:
        # 이동 후 벽에 부딪히지 않을 때
            if board[nr][nc] == transcolor:
            # 상대편의 돌인 경우
                change_lst.append([nr, nc])
                nr = nr + dr[j]
                nc = nc + dc[j]
            elif board[nr][nc] == origincolor:
                need = True
                # 색 전환 초기값 False
                break
                # while문 종료
            else:
            # 돌이 없는 경우
                break
                # while문 종료
        if need and change_lst:
        # 변경할 필요가 있고(자신의 돌이 존재하는 경우)
        # 변경할 상대편 돌의 인덱스가 존재하는 경우
            for k in change_lst:
                board[k[0]][k[1]] = origincolor

    # 최종적으로 보드에 자신의 돌이 많은 사람이 이기는 게임

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 보드의 한 변의 길이 N과 플레이어가 돌을 놓는 횟수 M
    # N은 4, 6, 8 중 하나

    board = [[0 for _ in range(N)] for _ in range(N)]
    # 보드는 4x4, 6x6, 8x8(가로, 세로 길이) 크기를 사용

    board[N//2-1][N//2-1] = 2
    board[N//2][N//2] = 2
    # 백돌 초기위치
    board[N//2-1][N//2] = 1
    board[N//2][N//2-1] = 1
    # 흑돌 초기위치
    # N=4 (1,1)W (2,2)W (1,2)B (2,1)B
    # N=6 (2,2)W (3,3)W (2,3)B (3,2)B
    # n=8 (3,3)W (4,4)W (3,4)B (4,4)B
    # B : 흑돌, W : 백돌
    # 가운데에 아래와 같이 배치하고 시작

    pos = [list(map(int, input().split())) for _ in range(M)]
    # M줄에는 돌을 놓을 위치(행 열)와 돌의 색(1이면 흑돌, 2이면 백돌)

    dr = [1, -1, 0, 0, 1, -1, -1, 1]
    # 상하
    dc = [0, 0, 1, -1, -1, -1, 1, 1]
    # 좌우
    # 4방향 대각선 유의
    # "사이"란 가로/세로/대각선(델타)

    # 플레이어는 빈공간에 돌(if)
    # 자신이 놓을 돌과 자신의 돌 사이에 상대편의 돌이 있을 경우에만(if)
    # 그 때의 상대편의 돌은 자신의 돌로(갱신)

    # 처음엔 흑부터 시작
    # 흑돌과 백돌을 가진 사람이 번갈아가며 보드에 돌을 놓아서
    # 돌을 놓을 곳이 없다면(else) 상대편 플레이어가 다시
    
    for i in pos:
        c = i[0] - 1
        r = i[1] - 1
        color = i[2]
        if color == 2:
        # w인 경우
            board[r][c] = 2
            # 새로 놓는 돌의 색 표시
            trans(r, c, 2, 1)
        else:
        # b인 경우
            board[r][c] = 1
            # 새로 놓는 돌의 색 표시
            trans(r, c, 1, 2)

    b_cnt = 0
    w_cnt = 0

    for i in board:
        for j in i:
            if j==1:
            # 흑돌인 경우
                b_cnt+=1
            elif j==2:
            # 백돌인 경우
                w_cnt+=1
                
    print("#{} {} {}".format(tc, b_cnt, w_cnt))
    # 게임이 끝난 후 보드 위의 흑돌, 백돌의 개수를 출력