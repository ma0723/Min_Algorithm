# 카운팅 정렬

import sys
sys.stdin = open("1945.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    # 테스트 케이스 반복
    N = int(input())
    prime = [2, 3, 5, 7, 11]
    cnt = [0] * 5
    # 카운팅 정렬

    for i in range(len(prime)):
        while N % prime[i] == 0:
            # 소수로 나누어 떨어지는 경우 나머지가 0(%)
            # 나누어 떨어지지 않으면 while문 종료 다시 for문 다른 소수로 나눈다
            # prime[0] = 2, prime[1] = 3 ...
            cnt[i] += 1
            # 소수의 카운팅 정렬 list에 개수 추가
            N //= prime[i]
            # N은 소수로 나눈 몫으로 할당

    print("#{} {}".format(tc, " ".join(map(str, cnt))))
    # 공백을 한 칸 둔 다음 정답을 출력
    # 숫자를 문자열로 전환(map(str,))
    # 문자열을 공백을 기준으로 나열(" ".join())