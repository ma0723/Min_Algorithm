import sys
sys.stdin = open("3752.txt", "r")

def DFS(idx, sum):
    global result
    if idx == N:
        result.add(sum)
        return
    if sum in result:
        return
    # DP 가지치기 Runtime error Fail 방지
    # 하지만 제한시간초과 Fail
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            DFS(idx + 1, sum + score[i])
            DFS(idx + 1, sum)
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 시험을 위해 N개의 문제를 만들었다
    score = list(map(int, input().split()))
    # 문제의 배점을 의미하는 N개의 자연수가 공백으로 구분
    visited = [0]*N
    result = set()
    DFS(0, 0)

    # 틀리면 0점 맞으면 배점만큼의 점수를 받게 된다
    # 가능한 시험점수의 합 (중복 제거) set

    print("#{} {}".format(tc, len(result)))

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 시험을 위해 N개의 문제를 만들었다
    score = list(map(int, input().split()))
    # 문제의 배점을 의미하는 N개의 자연수가 공백으로 구분

    total = [0]
    # 가능한 점수 리스트
    visited = [0] * 10001
    # 방문 배열

    for i in range(N):
    # N개의 문제 순회하는 for문
        for j in range(len(total)):
        # 가능한 점수 리스트의 개수만 순회하는 for문
        # total_score의 len은 계속 갱신
            new = score[i] + total[j]
            # 가능한 점수(중복 제거) + 다른 문항 점수 추가
            if visited[new] == 0:
            # 방문하지 않은 경우
                visited[new] = 1
                # 방문 표시 (중복 제거)
                total.append(new)
                # 가능한 점수 추가

    print('#{} {}'.format(tc, len(total)))