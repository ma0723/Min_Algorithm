import sys
sys.stdin = open("5189.txt", "r")

def dfs(start, battery_total, cnt):
    global result
    # result 최소값 변경
    if cnt == N-1:
    # 이동경로의 개수가 사무실로부터 모든 관리구역 이동하는 경우 N-1개
    # 총 이동경로의 개수는 N개이며 마지막 사무실로 돌아오는 배터리양 추후 추가
        battery_total += battery[start][0]
        # 마지막 사무실로 돌아오는 배터리양
        if result > battery_total:
        # 최소값 갱신
            result = battery_total
        return

    if result < battery_total:
    # 최소 배터리 사용량 가지치기
        return
    
    for next in range(1, N):
    # 사무실 위치 1번 인덱스 0
    # 관리구역 위치 2번부터 인덱스 1번부터 N-1
        if not visited[next]:
        # 관리구역을 방문하지 않은 경우
            visited[next] = 1
            # 방문 표시
            dfs(next, battery_total + battery[start][next], cnt+1)
            # 재귀 (다음 출발지, 배터리 사용량 누적, 이동횟수)
            visited[next] = 0
            # 방문 초기화

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]
    # N개씩 N개의 줄에 걸쳐 100이하 자연수

    visited = [0] * N
    # 방문 배열
    result = 99999999999
    # 최소값
    dfs(0, 0, 0)
    # 전기 카트로 사무실에서 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야 한다
    # 사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량

    print("#{} {}".format(tc, result))


