# 델타
import sys
sys.stdin = open("1210.txt", "r")

# 아래 방향으로 진행하면서
# 좌우 방향으로 이동 가능한 통로가 나타나면 방향 전환
# 방향 전환 이후엔 다시 아래 방향으로만 이동하게 되며, 바닥에 도착하면 멈추게 된다

T = 10
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]
    # 100 x 100 크기의 2차원 배열로 주어진 사다리
    # 지정된 도착점에 대응되는 출발점 X를 반환
    # 사다리는 연속된 ‘1’로 표현
    # 도착 지점은 '2'로 표현

    target = 0
    for i in range(100):
        if lst[99][i] == 2:
            target = i
            break

    dy = [0, 0, -1]
    # 행 상 방향
    dx = [-1, 1, 0]
    # 열 좌우 방향

    y = 99  # 행
    x = target  # 열

    while y >= 0:
    # 열의 인덱스가 lst[0][x] 경우 종료
        for j in range(3):
            nx = x + dx[j]
            # 열 좌우 방향
            ny = y + dy[j]

            if 0 <= nx < 100 and 0 <= ny < 100:
            # 인덱스의 위치가 리스트를 벗어나지 않는 범위 설정
            # 좌우상 순서이므로 좌우가 먼저 존재할 경우 좌우의 위치 좌표 입력
            # 출발한 가로선이 다른 막대를 가로질러서 연속하여 이어지는 경우는 없다
            # 주변의 좌우 중 하나만 1이다

                if j==0 and lst[ny][nx]==1:
                # 왼쪽 전환
                    x -= 1
                    while not lst[y-1][x]:
                    # 왼쪽 대각선 상향에 1이 존재한다면 while 종료
                        x -= 1
                        # 왼쪽 대각선 상향에 0이 존재한다면 계속 왼쪽 이동
                    y -= 1
                    # 지나왔던 오른쪽 길로 가지 않기 위해 행 상향 이동
                    break
                    # for문 종료(다음 인덱스 진행하면 왔던길로 돌아간다)

                elif j==1 and lst[ny][nx]==1:
                # 오른쪽 전환
                    x += 1
                    while not lst[y-1][x]:
                    # 오른쪽 대각선 상향에 1이 존재한다면 while 종료
                        x += 1
                        # 오른쪽 대각선 상향에 0이 존재한다면 계속 오른쪽 이동
                    y -= 1
                    # 지나왔던 왼쪽 길로 가지 않기 위해 행 상향 이동
                    break
                    # for문 종료(다음 인덱스 진행하면 왔던길로 돌아간다)
        else:
        # 좌우 열 전환이 모두 종료된 이후
            y -= 1
            # 원칙적으로 행 상향 이동

    print('#{} {}'.format(tc, x))


def find(sr, sc):
    dr = [0, 0, -1]
        # 행 상 방향
    dc = [-1, 1, 0]
    # 열 좌우 방향
    for k in range(3):
    # 방향 3가지
        nr = sr + dr[k]
        nc = sc + dc[k]
        # 이동 위치
        if 0 <= nr < 100 and 0 <= nc < 100:
        # nr 혹은 nc 사다리 내부 확인
            if lst[nr][nc] == 1:
            # 사다리인지 확인
                break
    if nr == 0:
    # 가장 상단 행 도착
        return nc
        # 열 좌표 반환
    lst[sr][sc] = 0
    sr = nr
    sc = nc
    # 왔던 길의 1을 0으로 전환
    # 좌우 방향 모두 이동가능하기 때문에 지속적으로 한 방향 이동

T = 10
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]
    # 100 x 100 크기의 2차원 배열로 주어진 사다리
    # 지정된 도착점에 대응되는 출발점 X를 반환
    # 사다리는 연속된 ‘1’로 표현
    # 도착 지점은 '2'로 표현

    target = 0
    for i in range(100):
        if lst[99][i] == 2:
            target = i
            break

    print('#{} {}'.format(tc, find(99, target)))



