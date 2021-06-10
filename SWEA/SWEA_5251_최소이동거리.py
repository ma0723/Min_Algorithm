import sys
sys.stdin = open("5251.txt","r")

def DFS(idx, route):
    global result
    if route >= result:
    # 이동거리가 현재 존재하는 최소 이동거리보다 크다면
    # 가지치기
        return
    if idx == N:
    # 마지막 연결지점 번호 N에 도달한 경우
        if result > route:
        # 최소 이동 거리 갱신
            result = route
        return
    for i in node[idx]:
    # 정점 idx에 연결된 모든 e 지점과의 구간 거리 w를 순회하는 for문
        e = i[0]
        # 구간의 끝 지점 e
        w = i[1]
        # 구간 거리 w
        DFS(e, route + w)
        # 완전탐색 / 재귀

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    # 마지막 연결지점 번호 N 도로의 개수 E
    # 일방통행 도로 구간 (방향성 그래프)

    node = [[] for _ in range(N+1)]
    # 0부터 N번까지의 번호 (0부터 유의)

    for _ in range(E):
    # 도로의 개수 E
        s, e, w = map(int, input().split())
        # 구간 시작 s, 구간의 끝 지점 e, 구간 거리 w가 차례
        # 시작과 끝의 연결 지점 번호, 구간의 길이
        node[s].append([e, w])

    result = 999999999999
    DFS(0, 0)
    # 0번 지점에서 N번 지점까지 이동하는데 걸리는 최소한의 거리
    # 모든 연결 지점을 거쳐가야 하는 것은 아니다

    print("#{} {}".format(tc, result))