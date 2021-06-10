import sys
sys.stdin = open("1954.txt", "r")

# while문
T = int(input())
for tc in range(1, T+1):

    n = int(input())
    arr = [[0 for j in range(n)] for i in range(n)]
    # 5행 5열 2차원 리스트
    row = 0
    # 행 초기값
    col = -1
    # 열 초기값
    cnt = 1
    # 인덱스의 value 증가량(1...nXn)
    turn = 1
    # 행열의 증감량(1 우측하향, -1 좌측상향)

    while n!=0:
        for i in range(n):
        # 가로 방향 행 고정 열 변화
            col += turn
            arr[row][col] = cnt
            # arr[0][0] col 초기값 -1에 turn 1을 더한 후 삽입하여 [0][0]
            # arr[0][0] = 1
            # arr[0][4]까지 순회
            cnt += 1
            # cnt = 1부터 cnt = 5까지 순회
            # cnt = 6 할당
        n -= 1
        # 가장 상단의 첫 행을 채운 후
        # 남은 n-1개의 행
        for j in range(n):
        # 남은 n-1개의 행
        # 세로 방향 행 변화 열 고정
            row += turn
            arr[row][col] = cnt
            # arr[0][4]까지 순회 후
            # arr[1][4] row 초기값 0에 turn 1을 더한 후 삽입하여 [1][4]
            # cnt = 5까지 순회 후
            # arr[1][4] = 6
            # arr[4][4]까지 순회
            cnt += 1
            # cnt = 6부터 cnt = 9까지 순회
            # cnt = 10 할당
        turn *= -1
        # arr[4][4]까지 순회 후
        # arr[4][3] arr[4][2] arr[4][1] arr[4][0] 상단의 for문에서 col의 값이 1씩 감소
        # arr[3][0] arr[2][0] arr[1][0] 하단의 for문에서 row의 값이 1씩 감소
        # col += turn / row += turn 를 반영
        # 다시 2개의 for문을 순회한 후에는 첫바퀴처럼 turn=1로 설정하고 방향 조절

    print('#{}'.format(tc))
    for i in arr:
        print(*i)

# 방향
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    dx = [0, 1, 0, -1]
    # 행 하상 방향
    dy = [1, 0, -1, 0]
    # 열 우좌 방향
    mode = 0
    # 방향 인덱스
    # mode 0 열 오른쪽
    # mode 1 행 아래쪽
    # mode 2 열 왼쪽
    # mode 3 행 위쪽

    # 초기좌표 및 초기값
    x = y = 0
    arr[x][y] = 1

    for num in range(2, N ** 2 + 1):
        x += dx[mode]
        # 행 하상 방향 인덱스
        y += dy[mode]
        # 열 우좌 방향 인덱스
        arr[x][y] = num
        # 상하좌우방향 이동 후 인덱스에 값 추가
        # 초기값 arr[x][y] = 1이 존재하므로 num은 2부터 할당
        if 0 <= x + dx[mode] < N and 0 <= y + dy[mode] < N and not arr[x + dx[mode]][y + dy[mode]]:
        # 상하좌우방향 이동 후 인덱스가 범위 안에 있고(0 <= < N)
        # 숫자가 아직 없다면(not)
            continue
        else:
            if mode!=3:
            # 방향인덱스 마지막이 아니라면 (mode 3 행 위쪽)
                mode+=1
                # 방향인덱스 1씩 추가
            else:
            # 방향인덱스 마지막이라면 (mode 3 행 위쪽)
                mode=0
                # 방향인덱스 처음으로 (mode 0 열 오른쪽)

    print('#{}'.format(tc))
    for i in arr:
        print(*i)

T = int(input())
for tc in range(1, T + 1):
    print('#{}'.format(tc))

    N = int(input())
    arr = [[0] * N for _ in range(N)]
    # N*N 2차원 배열 list

    dr = [0, 1, 0, -1]
    # 행 하상 방향
    dc = [1, 0, -1, 0]
    # 열 좌우 방향
    r = 0
    c = -1
    # (-1, 0)을 시작으로 (0, 0)으로 오른쪽으로 나아가는 방향
    dir = 0
    # dr dc의 인덱스에 따라 변하는 방향(상하좌우) 조절하는 인덱스
    num = 1
    # 시작점
    finish = N*N

    while True:
        print(num, end=' ')
        nr = r + dr[dir]
        nc = c + dc[dir]
        # dir인덱스는 방향을 변경하기 전까지 지속
        # 벽을 만날 때 dir 변경

        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc]==0:
        # 인덱스 안에서
        # 숫자가 입력되지 않아 0인 경우
            arr[nr][nc] = num
            r = nr
            c = nc
            # 이동한 좌표를 현 좌표로 갱신
            num += 1
            # 1부터 1씩 증가하며 숫자를 채운다
        else:
        # 인덱스가 벽에 부딪힐 때
            if dir !=3:
                dir += 1
                # 다음 방향으로 인덱스 1씩 추가
            else:
            # dir이 3인 경우 dr과 dc의 list의 마지막 인데스
                dir = 0
                # 다시 처음으로 방향 인덱스 0 초기화
            # dir = (dir+1)%4
            # 4인 경우 0 5인 경우 1
            # 나머지로 인덱스 조절

        if num > finish:
        # num이 계속 증가하다가 N*N의 값이 되면
            break
            # while문 종료
    print("#{}".format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()

