# 완전 검색

import sys
sys.stdin = open("1959.txt", "r")

T = int(input())
for tc in range(1, T + 1):

    N, M = map(int, input().split())
    nList = list(map(int, input().split()))
    mList = list(map(int, input().split()))

    my_max = 0
    if N > M:
    # nList의 길이가 mList의 길이보다 길다면
        for i in range(N-M+1):
        # index 0부터 N-M(긴 길이의 개수-짧은 길이의 개수)까지
        # 5(N)개와 3(M)개의 경우 짧은 3개(M)가 긴 5개(N)의 index 0부터 2(N-M)까지 이동하는 for문
            tmp = 0
            for j in range(M):
            # index 0부터 M-1까지 짧은 길이의 개수만큼 반복하는 for문
                tmp += mList[j] * nList[i+j]
                # 서로 마주보는 숫자들을 곱한 뒤 모두 더할 때
                # 짧은 mList의 인덱스 j 기준
            if tmp > my_max:
                my_max = tmp
                # 최대값 갱신 할당
                # for문을 모두 순환한 뒤 비교
    else:
    # nList의 길이가 mList의 길이보다 짧다면
        for i in range(M - N+1):
        # index 0부터 M-N(긴 길이의 개수-짧은 길이의 개수)까지
        # 5(M)개와 3(N)개의 경우 짧은 3개(N)가 긴 5개(M)의 index 0부터 2(M-N)까지 이동하는 for문
            tmp = 0
            for j in range(N):
            # index 0부터 N-1까지 짧은 길이의 개수만큼 반복하는 for문
                tmp += nList[j] * mList[i + j]
                # 서로 마주보는 숫자들을 곱한 뒤 모두 더할 때
                # 짧은 nList의 인덱스 j 기준
            if tmp > my_max:
                my_max = tmp
                # 최대값 갱신 할당
                # for문을 모두 순환한 뒤 비교

    print('#{} {}'.format(tc, my_max))