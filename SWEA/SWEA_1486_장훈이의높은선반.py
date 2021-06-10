import sys
sys.stdin = open("1486.txt", "r")

def dfs(idx, total):
# 완전 탐색 (h의 인덱스, 탑의 높이)
    global result
    if idx == N:
    # 모든 점원의 인덱스를 방문
        if result > total >= B:
            result = total
            # 만들 수 있는 높이가 B 이상인 탑 중에서 탑의 높이와 B의 차이가 가장 작은 것을
        return
    if total > result:
    # 가지치기
    # 가장 낮은 탑
        return
    dfs(idx + 1, total + h[idx])
    # 인덱스 0부터 N-1까지 순회 1씩 증가
    # 탑의 높이 점원들의 키 증가
    dfs(idx + 1, total)
    # 재귀 return하는 경우 탑의 높이에서 점원 제거

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    #  N명의 점원들
    #  높이가 B인 선반
    h = list(map(int, input().split()))
    # 점원들 키

    result = sum(h)
    # 탑의 높이는 2명 이상일 경우 탑을 만든 모든 점원의 키의 합과 같다
    # 가장 낮은 탑
    dfs(0, 0)
    # 완전 탐색 (h의 인덱스, 탑의 높이)

    print("#{} {}".format(tc, result-B))
