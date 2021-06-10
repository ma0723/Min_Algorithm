import sys
sys.stdin = open("3074.txt", "r")

def binarysearch(left, right, times):
    global result
    if right < left:
        return
    mid = (left + right)//2
    people = 0
    for time in times:
        people += mid//time
        # 주어진 mid 시간동안 각 심사대가 심사할 수 있는 사람의 수
        # 합계
        if people >= M:
        # 주어진 M명보다 더 많은 사람을 점검할 수 있다면
            result = mid
            # 조건을 충족하는 시간으로 result에 저장
            binarysearch(left, mid - 1, times)
            # mid보다 상한 값을 낮춘다
    if people < M:
        binarysearch(mid + 1, right, times)
        # 주어진 M명보다 적은 사람을 점검할 수 있어서
        # mid보다 하한 값을 높인다

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 심사대 총 N개가 있어서 1번에서 N번 까지의 번호
    # M명의 사람이 입국심사

    times = []
    for _ in range(N):
    # N개의 줄의 k번째 줄에는 tk (1 ≤ tk ≤ 109)
        times.append(int(input()))
    # print(times)

    left, right = 1, max(times)*M
    result = 0
    # print(left, right)

    binarysearch(left, right, times)
    # 이 사람들이 모두 심사를 받기 위해 걸리는 최소한의 시간을 구하는 프로그램

    print("#{} {}".format(tc, result))

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    time_lst = []
    for _ in range(N):
        time_lst.append(int(input()))
    #하한, 상한 초기화
    left, right = 1, max(time_lst)*M
    result = 0
    while left <= right:
        mid = (left + right)//2
        people = 0
        # 총 소요된 시간에서 각 심사위원이 맡은 사람의 수의 합이 M을 넘어야한다.
        # while문이 끝나고나면 조건을 충족하는 시간 중 가장 작은 값이 결과 값으로 저장된다.
        for t in time_lst:
            people += mid//t
            # M을 넘는다면 조건을 충족하는 시간으로 result에 저장하고 상한 값을 낮춘다.
            if people >= M:
                result = mid
                right = mid -1
                break
        # M을 넘지 못한다면 시간의 값이 커져야하므로 하한 값을 높인다.
        if people < M:
            left = mid + 1
    print('#{} {}'.format(tc, result))