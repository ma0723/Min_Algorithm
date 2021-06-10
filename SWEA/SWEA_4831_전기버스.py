import sys
sys.stdin = open("4831.txt", "r")
# 카운팅 정렬

T = int(input())
for tc in range(1, T + 1):

    # 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력
    # 종점에 도착할 수 없는 경우는 0을 출력

    K, N, M = map(int, input().split())
    # 각 노선별로 K(최대한 이동할 수 있는 정류장 수 K), N(N번 정류장까지 이동), M(충전기가 설치된 M개의 정류장)
    number = list(map(int, input().split()))
    # 다음줄에 M개의 정류장 번호
    # 공백을 기준으로 나눈다(.split())
    # 정수로 변환(map(int, ))
    # list로 변환(list())
    route = [0] * (N + 1)
    # ( 1 ≤ K, N, M ≤ 100 ) 0번부터 N번 정류장 담을 상자 list 생성

    for i in range(len(number)):
        route[number[i]] += 1
        # number[0] 부터 number[len(number)-1]인 각 M개의 정류장 번호를 route의 인덱스로 삽입하여 1 추가

    start = 0
    # 초기 현재 위치
    cnt = 0

    while True:
        for j in range(start + K, start, -1):
            # 1부터 움직일 수 있는 거리 K까지
            # 충전소 다음부터 움직일 수 있는 거리 K까지
            # 현재 위치와 이동할 수 있는 거리 사이 뒤로 1칸씩 for문
            # 역순으로 이동해야 이동할 수 있는 거리 사이에 주유소가 2개 있을 경우 가장 많이 이동하고 충전한 주유소의 거리에서 for문 종료
            if route[j] == 1:
            # K까지 가는 도중 충전소가 있는 경우
                start = j
                # 시작점을 충전소로 할당
                cnt += 1
                # 충전 횟수 1번씩 추가
                break
                # for 문 종료

        else:
        # 충전소가 없는 경우
            cnt = 0
            # 0을 출력
            break
            # while문 종료

        if start >= N:
        # start가 종점 정류장 이상인 경우
            break
            # while문 종료

    print('#{} {}'.format(tc, cnt))

