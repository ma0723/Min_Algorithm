import sys
sys.stdin = open("4828.txt", "r")

# 버블 정렬

T = int(input())
for tc in range(1, T + 1):
# test case 수 만큼 반복한다

    n = int(input())
    numbers = list(map(int, input().split()))
    # 공백을 기준으로 나눈다(.split())
    # 정수로 변환(int)
    # list로 변환(list())

    max_num = numbers[0]
    for num in numbers:
        # list의 값을 순회하는 for문
        if num > max_num:
            # 초기값 numbers[0]보다 큰 경우
            max_num = num
            # list의 값을 새로운 max_num으로 할당

    min_num = numbers[0]
    for num in numbers:
        # list의 값을 순회하는 for문
        if num < min_num:
            # 초기값 numbers[0]보다 큰 경우
            min_num = num
            # list의 값을 새로운 min_num으로 할당

    result = max_num - min_num

    print('#{} {}'.format(tc, result))