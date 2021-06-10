import sys
sys.stdin = open("1860.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    # test case 수 만큼 반복한다

    N, M, K = map(int, input().split())
    # 세 자연수 N, M, K(1 ≤ N, M, K ≤ 100)가 공백으로 구분
    guest = list(map(int, input().split()))
    # N개의 정수가 공백으로 구분
    # 공백을 기준으로 나눈다(.split())
    # 한 줄로 입력(input())
    # 정수로 변환(map(int, ))
    # list로 변환(list())

    bread = 0
    # 초기값 0 현재 붕어빵의 개수
    result = 'Possible'
    # 초기값 가능
    for i in range(11112):
        if i != 0 and i % M == 0:
            # 시간이 M으로 나누어 떨어지는 경우 나머지가 0(%)
            bread += K
            # 빵이 K개 증가
        for j in guest:
            if j == i:
                # 손님이 오는 시간일 때
                if bread == 0:
                    # 남은 빵이 0개
                    result = 'Impossible'
                    break
                    # for문 종료
                bread -= 1
                # 손님당 빵 1개씩 감소

    print("#{} {}".format(tc, result))