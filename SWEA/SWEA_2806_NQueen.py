import sys
sys.stdin = open("2806.txt", "r")

def DFS(queen):
    global result
    if queen == N:
    # N번째 행에 퀸을 놓은 경우
        result += 1
        return
    else:
        for i in range(N):
            if not horizon[queen] and not vertical[i] and not right_diagonal[queen+i] and not left_diagonal[N-1 + (queen-i)]:
            # Queen이 방문할 수 있는 경우
            # 가로, 세로, 대각선 2개의 값이 0인 경우
                board[queen][i] = 1
                # Queen 방문
                horizon[queen] = 1
                vertical[i] = 1
                # 가로(queen) 및 세로(i) 방문 표시
                right_diagonal[queen+i] = 1
                # (0,0) / (1,0) (0,1) / (2,0) (1,1) (0,2)
                left_diagonal[N-1 + (queen-i)] = 1
                # (0,0) (1,1)...(N-1, N-1) / (1,0) (2,1)...
                # 우상향 및 우하향 대각선 방문 표시

                DFS(queen + 1)
                # 재귀
                # 다음 행의 Queen

                board[queen][i] = 0
                horizon[queen] = 0
                vertical[i] = 0
                # 가로 및 세로 방문 표시
                right_diagonal[queen + i] = 0
                # (0,0) / (1,0) (0,1) / (2,0) (1,1) (0,2)
                left_diagonal[N - 1 + (queen - i)] = 0
                # (0,0) (1,1)...(N-1, N-1) / (1,0) (2,1)...
                # 우상향 및 우하향 대각선 방문 표시
                # Queen 방문 초기화
                # 가로 및 세로, 우상향 및 우하향 대각선 방문 초기화

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 하나의 자연수 N(1 ≤ N ≤ 10)
    board = [[0 for _ in range(N)] for _ in range(N)]
    # N*N 보드에 N개의 퀸을 서로 다른 두 퀸이 공격하지 못하게 놓는 경우의 수
    # 같은 행, 열, 또는 대각선 위에 있는 말을 공격

    horizon = [0]*N
    # 행 N개
    vertical = [0]*N
    # 열 N개
    right_diagonal = [0]*(2*N-1)
    # 우하향 대각선 2N-1개
    left_diagonal = [0]*(2*N-1)
    # 좌상향 대각선 2N-1개

    result = 0
    # 경우의 수
    DFS(0)
    # 완전 탐색 queen

    print("#{} {}".format(tc, result))
    # # N이 주어졌을 때, 퀸을 놓는 방법의 수