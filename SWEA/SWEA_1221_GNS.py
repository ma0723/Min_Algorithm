# 0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬
# "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"

import sys
sys.stdin = open("1221.txt", "r")

def BubbleSort(lst):
    for i in range(len(lst)-1, 0, -1):
        for j in range(0, i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

T = int(input())
for tc in range(1, T+1):
    test, N = input().split()
    # tc 번호, 문자열의 개수
    str = list(input().split())
    # 문자열 리스트
    # str이므로 map(int, )는 불요

    chr = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    num = [i for i in range(10)]
    # 대응되는 기준 문자, 숫자 list 초기값 설정

    # 문자열 숫자로 전환
    for i in range(len(str)):
        for j in range(10):
        # chr과 num 인덱스 0에서 10
            if str[i] == chr[j]:
            # 입력된 문자열의 값이 chr list의 값과 같다면
                str[i] = num[j]
                # 입력된 문자열의 값을 num list의 값으로 전환

    # 숫자 정렬
    # 버블 정렬
    result = BubbleSort(str)

    # 숫자 문자열로 전환
    for i in range(len(result)):
        for j in range(10):
        # chr과 num 인덱스 0에서 10
            if str[i] == num[j]:
            # 숫자로 전환된 문자열의 값이 num list의 값과 같다면
                str[i] = chr[j]
                # 숫자로 전환된 문자열의 값을 chr list의 값으로 전환

    print("#{}".format(tc))
    # #번호 출력
    print(*result)
    # 리스트를 모두 꺼낸 행렬의 상태로 출력(*)

T = int(input())
for tc in range(1, T+1):
    test, N = input().split()
    # tc 번호, 문자열의 개수
    N = int(N)
    # test와 N은 모두 문자이므로 N만 정수형 전환
    # test에는 #이 포함되어 정수형 전환 불가

    arr = list(input().split())
    # 문자열 리스트
    # str이므로 map(int, )는 불요

    nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    counts = [0 for _ in range(10)]
    # 카운팅 정렬 초기값 설정

    for i in range(len(arr)):
        for j  in range(len(nums)):
            if arr[i] == nums[j]:
            # 입력값이 nums의 리스트에 포함되어 있는 경우
                counts[j] += 1
                # 카운팅 정렬에 입력값의 개수 입력

    for i in range(len(counts)):
        for j in range(counts[i]):
            print(nums[i], end = " ")
            # j번(counts[i])만큼 계속 출력
    print()
    # 개행