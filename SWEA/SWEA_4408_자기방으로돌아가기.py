import sys
sys.stdin = open("4408.txt", "r")

# 최단 시간에 모든 학생이 자신의 방으로 돌아가려고 한다
# 긴 복도를 따라 총 400개의 방이 다음과 같이 배열
# 만약 두 학생이 자기방으로 돌아가면서 지나는 복도의 구간이 겹치면 두 학생은 동시에 돌아갈 수 없다
# (방1 -> 4) 와 (방3 -> 6) 은 복도 구간이 겹치므로 한 사람은 기다렸다가 다음 차례에 이동(대기+1씩 구간 나누기)
# 현재 방 위치와 돌아가야 할 방의 위치의 목록이 주어질 때, 최소 몇 단위시간만에 모든 학생들이 이동할 수 있는지

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 돌아가야 할 학생들의 수 N
    room = [list(map(int, input().split())) for _ in range(N)]
    # 다음 N 줄에는 각 학생의 현재 방 번호(≤400)와 돌아가야 할 방의 번호(≤400)
    # 1번부터 유의
    route = [0]*200
    # 400개의 방의 동선 표시 리스트
    # 인덱스 0번부터 유의
    # 1 3 5 ... 399
    # 2 4 6 ... 400
    # 200개의 길

    for i in room:
        if i[0]%2==1:
            start = i[0]//2
        else:
            start = i[0]//2-1
        if i[1]%2==1:
            end = i[1]//2
        else:
            end = i[1]//2-1
        # 윗줄은 홀수 아랫줄은 짝수이므로 인덱스의 경우의 수를 고려
        if start < end:
        # 출발과 도착의 방의 인덱스 순서의 크기가 다른 것을 고려
            for j in range(start, end+1):
                route[j] += 1
        if start > end:
        # 출발과 도착의 방의 인덱스 순서의 크기가 다른 것을 고려
            for j in range(end, start+1):
                route[j] += 1

    ans = 0
    for i in route:
        if ans < i:
            ans = i

    print("#{} {}".format(tc, ans))