# 비트 마스크
# 재귀
import sys
sys.stdin = open("4837.txt", "r")

# 1부터 12까지의 숫자를 원소로 가진 집합 A
# 집합 A의 부분 집합 중 N개의 원소를 갖고 있고
# 원소의 합이 K인 부분집합의 개수

T = int(input())
for tc in range(1, T+1):
    A = [i for i in range(1, 13)]
    len_lst = len(A)
    N, K = map(int, input().split())

    all_lst = []
    for i in range(1<<len_lst):
    # 부분집합의 개수
    # 개수만큼 2를 왼쪽으로 밀면서 2**n
        num_lst = []
        for j in range(len_lst):
        # 원소의 개수만큼 비트를 교환
        # 개수만큼 각 자리마다 순회하는 for문
            if i&(1<<j):
            # i의 j번째 비트가 1이면 j번째 원소를 출력
            # 각 자리마다 j를 왼쪽으로 밀면서 2**j 확인(j번째 비트)
            # i와 and 연산자로 둘다 1인 경우에 1로 추가(j번째 원소)
                num_lst.append(A[j])
                # 부분집합의 원소 추가
        all_lst.append(num_lst)
        # 부분집합 list를 담는 전체 list

    cnt = 0
    # 개수 초기값 0 설정
    for i in all_lst:
        if len(i) == N:
        # 부분집합(i)의 개수가 N인 경우
            my_sum = 0
            # 각 부분집합의 원소 총합 초기값 0
            for j in i:
                my_sum += j
            if my_sum == K:
            # 각 부분집합의 원소 총합이 K인 경우
                cnt += 1
                # 개수 추가

    print("#{} {}".format(tc, cnt))

T = int(input())
for tc in range(1, T + 1):
    A = [i for i in range(1, 13)]
    len_lst = len(A)
    N, K = map(int, input().split())

    result = 0
    # 초기값 설정
    # 조건에 부합하는 부분집합의 개수 카운팅

    for i in range(1 << len_lst):
    # 부분집합의 개수
    # 개수만큼 2를 왼쪽으로 밀면서 2**n
        total = 0
        cnt = 0
        # 초기값 설정
        for j in range(len_lst):
            # 원소의 개수만큼 비트를 교환
            # 개수만큼 각 자리마다 순회하는 for문
            if i & (1 << j):
            # i의 j번째 비트가 1이면 j번째 원소를 출력
            # 각 자리마다 j를 왼쪽으로 밀면서 2**j 확인(j번째 비트)
            # i와 and 연산자로 둘다 1인 경우에 1로 추가(j번째 원소)
                total += A[j]
                # 원소 누적합
                cnt += 1
                # 원소 개수 카운팅

    if cnt == N and total == K:
        result += 1

    print("#{} {}".format(tc, result))


