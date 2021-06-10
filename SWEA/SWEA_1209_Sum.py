import sys
sys.stdin = open("1209.txt", "r")

T = 10
for tc in range(1, T+1):
    N = int(input())
    my_list = [list(map(int, input().split())) for _ in range(100)]
    # lst = []
    # for _ in range(100):
    #   lst.append(list(map(int, input().split())))

    # for row in arr:
    #   print(row)
    # 행렬 출력

    result = []
    # 빈 리스트 초기값
    # 각 행, 각 열, 두개의 대각선 합 저장 list

    for y in range(len(my_list)):
    # 각 행의 합
    # 행 우선 탐색
        sum_row = 0
        # 초기값 0 설정
        for x in range(len(my_list)):
            sum_row += my_list[y][x]
        result.append(sum_row)
        # 행 고정 열 변화
        # 열 순회 후 각 행의 합 result(list) 추가

    for x in range(len(my_list)):
    # 각 열의 합
    # 열 우선 탐색
        sum_col = 0
        # 초기값 0 설정
        for y in range(len(my_list)):
            sum_col += my_list[y][x]
        result.append(sum_col)
        # 열 고정 행 변화
        # 행 순회 후 각 열의 합 result(list) 추가

    sum_diagonal1 = 0
    for y in range(len(my_list)):
    # 첫번째 대각선의 합
    # 행 우선 탐색
        for x in range(len(my_list)):
            if y == x:
            # 행과 열의 인덱스가 같다면 (0,0) (1,1) (2,2) ... (99,99)
            # 대각선이라면
                sum_diagonal1 += my_list[y][x]
    result.append(sum_diagonal1)
    # 대각선을 모두 순회한 후 합 result(list) 추가

    sum_diagonal2 = 0
    for y in range(len(my_list)):
    # 두번쨰 대각선의 합
    # 행 우선 탐색
        for x in range(len(my_list)):
            if y == len(my_list)-1-x:
            # 행과 열의 인덱스가 같다면 (0,99) (1,98) ... (99, 0)
            # 대각선이라면
            # len(my_list)-1-x
                sum_diagonal2 += my_list[y][x]
    result.append(sum_diagonal2)
    # 대각선을 모두 순회한 후 합 result(list) 추가

    # for i in range(len(my_list)):
    #     sum_diagonal1 += my_list[i][i]
    # result.append(sum_diagonal1)
    # for i in range(len(my_list)):
    #     sum_diagonal2 += my_list[i][len(my_list)-1-i]
    # result.append(sum_diagonal2)

    my_max = 0
    # 최대값 초기값 0설정
    for i in result:
        if i > my_max:
            my_max = i
            # 최대값 갱신 할당
            # 각 for문에 삽입 가능

    print(f'#{tc} {my_max}')