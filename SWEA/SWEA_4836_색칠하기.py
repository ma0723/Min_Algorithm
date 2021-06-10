# 2차원 배열
import sys
sys.stdin = open("4836.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = [[0]*10 for _ in range(10)]
    # 10x10 2차원 배열
    # 카운팅 정렬
    N = int(input())
    for _ in range(N):
    # color 1 혹은 2의 사각형 개수
        x1, y1, x2, y2, color = map(int, input().split())
        # N번만큼 순회하면서 값을 입력
        if color == 1:
        # color 1
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    arr[x][y] += 1
                    # 주어진 정보에서 같은 색인 영역은 겹치지 않는다
                    # 같은 색으로 인해 1이 여러번 더해질 경우는 없다

        else:
        # color 2
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    arr[x][y] += 1
                    # 주어진 정보에서 같은 색인 영역은 겹치지 않는다
                    # 같은 색으로 인해 1이 여러번 더해질 경우는 없다
        # print(arr)

    cnt = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 2:
            # color 1과 color 2가 겹쳐서 [0]에서 1이 두 번 더해진 경우
                cnt += 1
                # 보라색이 된 칸 수를 구하는 프로그램

    print("#{} {}".format(tc, cnt))

# 함수로 변형
def coloring(arr, r1, c1, r2, c2, color):
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            if arr[i][j] == 0 or arr[i][j] == color:
                arr[i][j] = color
                # 1 혹은 2
            else:
                arr[i][j] = 3

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(N):
        info = list(map(int, input().split()))
        coloring(arr, info[0], info[1], info[2], info[3], info[4])

    cnt = 0
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if arr[r][c] == 3:
                cnt += 1

    print("#{} {}".format(tc, cnt))



