import sys
sys.stdin = open("2819.txt", "r")

def dfs(r, c, num, cnt):
    if cnt == 7:
    # 7자리의 수
    # 6번 이동 cnt=1부터 시작
        return
    for i in range(4):
    # 상하좌우 탐색
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < 4 and 0 <= nc < 4:
        # 충돌하지 않는 경우
        # 이동을 할 때에는 한 번 거쳤던 격자칸을 다시 거쳐도 된다
            next = num + lst[nr][nc]
            # str 숫자 이어붙이며 자리수 1개씩 늘리기
            # 0으로 시작하는 0102001과 같은 수를 만들 수도 있다 str로 추가
            if not next in number[cnt + 1]:
            # 자리수 1개 더 증가한 값이 number list의 값에 포함되어 있지 않은 경우 
                number[cnt + 1].append(next)
                # 추가
            dfs(nr, nc, next, cnt + 1)
            # 포함되었든 안 되었든 계속 경우의 수 완전 탐색
            # 재귀 (행, 렬, 숫자다음값, 숫자자리수 1개 증가)

T = int(input())
for tc in range(1, T+1):
    lst = [list(input().split()) for _ in range(4)]
    # 4×4 크기의 격자판이 있다. 격자판의 각 격자칸에는 0부터 9 사이의 숫자
    # 숫자 이어붙이기 위해 int가 아닌 str
    number = [[] for _ in range(8)]
    # 각 칸에 적혀있는 숫자를 차례대로 이어 붙이면 7자리의 수
    # number[cnt] 자리수 개수를 인덱스로 하여 7자리의 수의 값을 number[7]에 저장

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    # 동서남북 네 방향으로 인접한 격자로 총 여섯 번 이동

    for i in range(4):
        for j in range(4):
            dfs(i, j, lst[i][j], 1)
            # 완전탐색 (행, 렬, 숫자값, 숫자자리수)

    print("#{} {}".format(tc,len(number[7])))
    # 만들 수 있는 서로 다른 일곱 자리 수들의 개수를 구하는 프로그램
