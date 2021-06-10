import sys
sys.stdin = open("5209.txt", "r")

def DFS(idx, total):
# 새로 생산되는 N종의 제품을 N곳의 공장에서 한 곳당 한가지씩 생산
# 공장별 생산비용이 주어질 때 전체 제품의 최소 생산 비용을 계산
    global result
    if idx == N:
    # N곳의 공장
        if total < result:
        # 최소값 갱신
            result = total
        return
    if total > result:
    # 갱신된 최소값보다 생산비용이 커지는 경우
    # 가지치기
        return
    for i in range(N):
    # N종의 제품
        if visited[i] == 0:
        # 아직 생상하지 않은 경우
            visited[i] = 1
            # 생산 표시
            DFS(idx+1, total + price[i][idx])
            # 생산한 제품 가격 추가 (price[i][idx])
            # 다음 공장 이동 (idx+1)
            visited[i] = 0
            # 생산 표시 초기화

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # A와 B에 속한 정수의 개수 N, M
    price = [list(map(int, input().split())) for _ in range(N)]
    # 각 N개의 공장당 N종의 제품 생산비용 리스트

    result = 999999999
    # 최소 생산 비용
    visited = [0]*N
    # 생산 표시 배열
    DFS(0, 0)
    # 완전 탐색

    print("#{} {}".format(tc, result))