import sys
sys.stdin = open("4881.txt", "r")

# 재귀
def dfs(idx, total):
    global min_sum
    # 글로벌로 추가
    if idx == N:
    # 모두 추출한 후
        if total < min_sum:
            min_sum = total
    if total >= min_sum:
    # 설정한 최소 합보다 크거나 같은 경우
        return
        # 가지치기
    for i in range(N):
    # N개의 원소 모두 순회
        if check[i] == 0:
        # 방문하지 않았다면
        # 방문한 곳의 세로 열을 겹치지 않게 하기 위해
            check[i] = 1
            # 방문 기록
            dfs(idx+1, total + lst[idx][i])
            # 재귀 함수
            check[i] = 0
            # 방문 기록 초기화
            # 재귀 함수가 idx==N if문을 거치거나 total이 min_sum을 넘기는 if문을 거쳐
            # 호출한 곳으로 되돌아올 때 초기화

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # NxN 배열에 숫자
    lst = [list(map(int, input().split())) for _ in range(N)]

    check = [0] * N
    # 원소 이미 사용했는지 체크 list
    min_sum = 99999999
    # 최소값 초기값 설정
    dfs(0,0)
            
    print("#{} {}".format(tc, min_sum))

def perm(n, s):
# s : 총합
    global minV
    # 최소값 변경하기 위해 global
    if n == N:
    # 순열이 완성되면
        if minV > s:
            minV = s
            # 최소값 갱신
        return
    elif minV <= s:
    # 순열이 아직 완성되지는 않았지만, 현재까지의 합이 minV보다 크거나 같다면
    # 더 해볼 필요가 없는 가지치기 백트래킹
        return
    else:
        for i in range(N):
            if u[i] == 0:
            # 선택되지 않은 경우
                u[i] = 1
                # 선택 표시
                perm(n+1, s + m[n][i])
                # 재귀 호출
                u[i] = 0
                # 선택 표시 다시 초기화

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    m = [list(map(int,input().split())) for _ in range(N)]
    u = [0 for _ in range(N)]
    # visited 배열
    minV = 1000
    # 최소값 초기값
    perm(0,0)
    # 순열
    print("#{} {}".format(tc, minV))
