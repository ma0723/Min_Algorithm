# 완전 검색

import sys
sys.stdin = open("6485.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 버스 종류 개수
    bus_stop = [0] * (5001)
    # 버스 정류장
    # 카운팅 정렬

    for i in range(N):
        A, B = map(int, input().split())
        # 버스 출발지와 도착지

        for j in range(A, B + 1):
            # 버스 출발지와 도착지(이상, 이하)
            bus_stop[j] += 1
            # 버스 출발지와 도착지까지 지나가는 버스 개수 1개 추가

    P = int(input())
    # P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지
    print("#{}".format(tc), end=" ")

    for i in range(P):
        C = int(input())
        # 버스가 지나다니는 정류장의 번호
        print(bus_stop[C], end=" ")
        # 각 C 번호에 해당하는 정류장에 지나가는 버스의 개수
    print()
    # 개행

