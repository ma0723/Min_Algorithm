import sys
sys.stdin = open("4843.txt", "r")

# 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아
# 주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지

def select(list, k):
# k번째로 작은 원소
# 셀렉션 알고리즘
    for i in range(0, k):
        min = i
        for j in range(i+1, len(list)):
            if list[min] > list[j]:
            # 0~k-1까지의 인덱스의 해당하는 값 list[min]
            # i+1 즉 1~k까지의 인덱스에 해당하는 값 list[j]
                min = j
                # 최소값을 찾아서 min 갱신 할당
        list[i], list[min] = list[min], list[i]
        # 처음에 설정된 index(i)와 최소값의 갱신된 index(j)의 값 교환
    return list[k-1]
    # k번째로 작은 원소 인덱스에 접근하여 값을 반환

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    result = []
    # 빈 리스트 초기값 설정
    for i in range(5):
    # 10개까지만 출력
    # 대1 소1 ... 대5 소5 5쌍
        result += [select(lst, len(lst)-i)]
        # 가장 마지막번째로 작은 수(가장 첫번째로 큰 수)
        # i의 시작은 0 유의
        result += [select(lst, i+1)]
        # 가장 첫번째로 작은 수(i+1)
        # i의 시작은 0 유의

    print("#{}".format(tc), end=' ')

    for i in result:
        print(i, end=' ')

    print()

def find():
    for i in range(10):
    # 10개의 숫자
        idx = i
        # 찾으려는 값의 인덱스
        if i%2:
        # 홀수 번째 최소값
            for j in range(i+1, N):
                if lst[idx] > lst[j]:
                    idx = j
                    # 최대값 인덱스
        else:
        # 짝수 번째 최대값
            for j in range(i + 1, N):
                if lst[idx] < lst[j]:
                    idx = j
                    # 최소값 인덱스
        t = lst[i]
        lst[i] = lst[idx]
        lst[idx] = t

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    find()

    print("#d"%tc, end = " ")
    for j in range(0, 10):
        print(lst[j], end = " ")
    print()
    # 개행