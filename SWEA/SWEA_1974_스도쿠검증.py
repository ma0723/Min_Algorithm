import sys
sys.stdin = open("1974.txt", "r")

# 가로 9칸 세로 9칸으로 이루어져 있는 표
# 1 부터 9 까지의 숫자를 채워넣는 퍼즐

# 3, 3 행우선조회, 열우선조회
# 9, 9 행우선조회, 열우선조회

T = int(input())
for tc in range(1, T+1):
    sdoku = [list(map(int, input().split())) for _ in range(9)]

    result = 0

    # 9,9 각 행 각 열

    for i in range(9):
        row = []
        col = []
        # 각 행 혹은 각 열 순회할 때마다 초기화
        # 초기값 빈 리스트
        for j in range(9):
            col.append(sdoku[j][i])
            row.append(sdoku[i][j])
        if len(set(row)) != 9 or len(set(col)) != 9:
        # 각 행, 각 열의 값을 담은 리스트의 중복제거(set)
        # 중복제거한 길이가 9가 아니면 숫자가 겹치는 경우
            result += 1
            # 겹치는 숫자가 있는 경우 result는 0이 아니다

    # 3, 3 정사각형
    index = [0, 3, 6]
    for i in index:
        for j in index:
            lst = []
            for k in range(3):
                for l in range(3):
                    lst.append(sdoku[i+k][j+l])
            if len(set(lst)) != 9:
            # 3, 3 부분 정사각형의 값을 담은 리스트의 중복제거(set)
            # 중복제거한 길이가 9가 아니면 숫자가 겹치는 경우
                result += 1
                # 겹치는 숫자가 있는 경우 result는 0이 아니다

    if result == 0:
        print("#{} {}".format(tc, 1))
    else:
        print("#{} {}".format(tc, 0))
    # 같은 줄에 1 에서 9 까지의 숫자를 한번씩만 넣고
    # 3 x 3 크기의 작은 격자 또한, 1 에서 9 까지의 숫자가 겹치지 않아야 한다
    # 겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력