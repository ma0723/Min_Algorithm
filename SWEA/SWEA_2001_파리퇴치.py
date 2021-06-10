import sys
sys.stdin = open("2001.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # M x M 크기의 파리채
    # N x N 배열
    lst = [list(map(int, input().split())) for _ in range(N)]

    x = 0
    y = 0
    result = []

    for i in range(N-M+1):
    # 시작점 행
        for j in range(N-M+1):
        # 시작점 열
            total = 0
            for k in range(M):
            # 파리채 길이만큼 인덱스 추가
                for l in range(M):
                    total += lst[i+l][j+k]
            result.append(total)

    ans = 0
    for i in result:
        if i > ans:
            ans = i
    print("#{} {}".format(tc, ans))




