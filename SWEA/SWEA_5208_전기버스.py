import sys
sys.stdin = open("5208.txt", "r")

def DFS(idx, cnt):
    global result
    if idx == 1:
    # 1번 정류장에서 버스가 도착한 경우
        if result > cnt:
            result = cnt
        return
    if result < cnt:
    # 가지치기
        return
    for i in range(1, N):
    # i는 idx와 거리가 멀을수록 cnt의 개수가 적어진다 (1부터 시작)
        if Bus[i] >= idx:
        # i번째 정류소에서 충전하여 이동할 수 있는 버스 위치 (Bus[i])
        # 현재 버스 위치 idx 보다 크거나 같다면 (N부터 시작)
            DFS(i, cnt+1)
            # (충전정류소 idx, 충전횟수+1)
            return
            # 함수 종료 for문

T = int(input())
for tc in range(1, T+1):
    Charge = list(map(int, input().split()))
    # 정류장[0]과 충전지[1:len(lst)]에 대한 정보
    N = Charge[0]
    # 정류장 수 N
    Bus = [0]
    # 배터리 충전후 갈 수 있는 버스 위치 idx

    for i in range(1, N):
    # 1번부터 N-1번까지의 정류장 idx 순회
    # N번 정류장은 배터리가 없다
        Bus.append(Charge[i]+i)
        # i번 정류장에서 배터리 충전하여 Charge[i] 갈 수 있는 버스 위치 idx 값으로 추가

    result = 99999

    DFS(N, 0)
    # (목표인 N번 idx, 충전횟수)
    # 충전지가 방전되기 전에 교체하며 운행해야 하는데 교체하는 시간을 줄이려면

    print("#{} {}".format(tc, result-1))
    # 1번 정류소에서 충전한 횟수는 빼야 한다