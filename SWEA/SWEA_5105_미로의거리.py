import sys
sys.stdin = open("5105.txt", "r")

def bfs(start):
    global result
    # 값 변경 global
    r = start[0]
    c = start[1]
    # 행렬 인덱스 초기값
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    # 상하좌우
    q = []
    # 큐 생성
    q.append((r, c))
    # 행렬 인덱스 rear tuple 삽입
    dis = [[0] * N for _ in range(N)]
    # 거리배열
    visited = [[0] * N for _ in range(N)]
    # 방문배열
    visited[r][c] = 1
    # 방문표시

    while q:
    # 큐에 자료가 존재하는 동안
        r, c = q.pop(0)
        # 큐 front 삭제
        for i in range(4):
        # 상하좌우 이동
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and lst[nr][nc]!=1 and visited[nr][nc] == 0:
            # 미로 밖으로 벗어나서는 안된다
            # 0은 통로, 1은 벽
            # 방문하지 않은 경우
                q.append((nr, nc))
                # 행렬 인덱스 rear tuple 삽입
                visited[nr][nc] = 1
                # 방문 표시
                dis[nr][nc] = dis[r][c] + 1
                # 거리값 이전 기준 인덱스의 거리값보다 1씩 증가
                if lst[nr][nc] == 3:
                # 도착지인 경우
                    result = dis[r][c]
                    return
                    # 경로가 있는 경우
                    # 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 미로 크기
    lst = [[int(i) for i in input()] for _ in range(N)]
    # 미로 행렬
    visited = [[0]*N for _ in range(N)] 
    # 방문 배열

    start = []
    end = []
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 2:
                start.append(i)
                start.append(j)
    result = 0
    bfs(start)

    print("#{} {}".format(tc, result))