import sys
sys.stdin = open("1865.txt", "r")

def DFS(idx, total):
    global result
    if idx == N:
        if result < total:
        # 최대값 갱신
            result = total
        return
    if total < result:
    # 가지치기 
    # total에 곱하는 값은 1보다 작아서 total이 result보다 작은 경우 그 값은 더 작아진다
        return
    for i in range(N):
        if visited[i]==0 and work[i][idx]:
        # 방문하지 않은 경우
        # 일의 능률이 0이 아닌 경우
            visited[i] = 1
            # 방문표시
            DFS(idx+1, total*work[i][idx]/100)
            # 재귀
            visited[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # N명의 직원
    # 해야할 일이 N개
    work = [list(map(float, input().split())) for _ in range(N)]
    # 직원들의 번호가 1부터 N까지 매겨져 있고, 해야 할 일에도 번호가 1부터 N까지 매겨져 있을 때

    result = 0
    # i번 직원이 j번 일을 하면 성공할 확률이 Pi, j
    # “주어진 일이 모두 성공할 확률”의 최댓값
    visited = [0]*N
    # 방문 배열
    
    DFS(0, 1)
    # (0.13*0.7*1.0)*100 = 9.1%
    # 9.100000

    print("#{} {:.6f}".format(tc, result*100))
    # 소수점 6번째자리까지