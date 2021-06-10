def solution(brown, yellow):
    answer = []
    # 노란색과 갈색으로 색칠된 격자의 개수
    y_lst = []
    for i in range(1, yellow+1):
    # 1부터 yellow 개수까지
        if yellow%i==0:
        # 노란색 직사각형 경우의 약수들의 집합 (나누어 떨어지는 경우)
        # 24 (1, 24) (2, 12) (3, 8) (4, 6) 등 중복 제거
            row = yellow//i
            col = i
            if row >= col:
            # 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다
                y_lst.append([row, col])
    for i in y_lst:
        b_row = (i[0] + 2)*2
        # 가로 양쪽 가로+2만큼 2번씩
        b_col = i[1]*2
        # 세로 양쪽 노란색 세로만큼 2번씩
        if b_row + b_col == brown:
        # 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫
            answer = [b_row//2, b_col//2+2]
            # 카펫의 가로(2로 나누기), 세로 크기(2로 나누고 위아래 +1씩 총 +2)