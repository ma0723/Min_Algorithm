import sys
sys.stdin = open("4835.txt", "r")
# 완전 검색

T = int(input())
for tc in range(1, T + 1):
# test case 수 만큼 반복한다

    N, M = map(int, input().split())
    num_lst = list(map(int, input().split()))
    # 공백을 기준으로 나눈다(.split())
    # 정수로 변환(int)
    # list로 변환(list())

    min_sum = max_sum = sum(num_lst[0: M])
    # 첫 부분집합을 최대/최소합의 기본값으로 설정

    for i in range(N - M + 1):
        # num_lst의 첫 출발발점을 index [0]부터 [N-M]까지
        temp_sum = 0
        # 부분합 초기값 0 설정
        for j in range(M):
            # 부분합 계산
            temp_sum += num_lst[i + j]
            # M이 3개인 경우 num_lst[i] 기준점 index에 0, 1, 2를 더해서 연속 3개의 숫자

        if min_sum > temp_sum:
            min_sum = temp_sum
        if max_sum < temp_sum:
            max_sum = temp_sum
        # 최대값 최소값 비교하여 새롭게 할당

    print('#{} {}'.format(tc, max_sum - min_sum))