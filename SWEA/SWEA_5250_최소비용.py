import sys
sys.stdin = open("5250.txt","r")

from collections import deque

def dijkstra():
    q = deque()
    q.append([0, 0])  # x좌표, y좌표
    # 항상 출발은 맨 왼쪽 위, 도착지는 가장 오른쪽 아래
    dist[0][0] = 0

    while q:
    # 큐가 존재할 때까지 반복
        x, y = q.popleft()
        # front 삭제
        h = arr[x][y]
        # 각 인덱스의 위치에서 지역 높이
        cost = dist[x][y]
        # 연료 비용
        for i in range(4):
        # 각 칸에서는 상하좌우 칸이 나타내는 인접 지역 이동
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
            # arr의 경계 내에 존재하는 경우
                new_cost = 1
                # 인접 지역으로 이동시에는 기본적으로 1만큼의 연료
                # 같은 높이의 경우 연료는 추가되지 않는다
                if h < arr[nx][ny]:
                # 더 높은 곳으로 이동하는 경우 높이 차이만큼 추가로 연료가 소비
                    new_cost += arr[nx][ny] - h
                    # 출발에서 최종 도착지까지 경유하는 지역의 높이 차이에 따라 연료 소비량이 달라지기 때문에
                if dist[nx][ny] > new_cost + cost:
                # 무한대보다 최소값 갱신
                    dist[nx][ny] = new_cost + cost
                    q.append([nx, ny])
                    # rear 삽입
    return dist[N-1][N-1]
    # 도착지 최종 연료 소비량

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 가로, 세로 칸수 N
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 다음 줄부터 N개 지역의 높이 H가 N개의 줄에 걸쳐 제공

    # INF = float('inf')
    INF = 100000
    dist = [[INF for _ in range(N)] for _ in range(N)]
    # 각 위치마다의 연료 소비량 리스트

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    # 상하좌우 탐색

    print("#{} {}".format(tc, dijkstra()))
    # 최적의 경로로 이동하면 최소한의 연료