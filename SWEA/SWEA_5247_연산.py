import sys
sys.stdin = open("5247.txt","r")

from collections import deque

# 3번 testcase 시간초과
# 재귀 / 스택 / 큐 (재귀가 시간초과라면 스택 혹은 큐 이용)
def calculation(number, idx):
    if idx == 0:
        return number + 1
    elif idx == 1:
        return number - 1
    elif idx == 2:
        return 2 * number
    return number - 10

# 재귀
# def DFS(value, cnt):
#     global result
#     if cnt > result:
#     # 가지치기
#         return
#     if value == M:
#     # 연산 결과 자연수 M인 경우
#         if cnt < result:
#         # 연산 횟수 최소값 갱신
#             result = cnt
#         return
#     visited[value] = 1
#     # 방문표시
#     for i in range(4):
#     # 연산 4가지 순회하는 for문
#         ans = calculation(value, i)
#         # 연산의 중간 결과
#         if 0 <= ans <= 1000000 and not visited[ans]:
#         # 연산의 중간 결과도 항상 백만 이하의 자연수 (-1 or -10 유의)
#         # 연산의 중간 결과를 방문하지 않은 경우
#             visited[ans] = 1
#             DFS(ans, cnt+1)
#             visited[ans] = 0

# BFS Queue deque 객체 front rear 인덱스 사용
def DFS(number, target):
    queue = deque()
    queue.append(number)
    # 큐 오른쪽 입력 append() 오른쪽 출력 pop()
    # 큐 왼쪽 입력 appendleft() 왼쪽 출력 popleft()
    visited[number] = 1
    while queue:
    # 큐가 존재하는 동안
        new_number = queue.popleft()
        # 왼쪽 마지막 값 추출 front 삭제
        cnt = visited[new_number]
        # 연산 횟수
        if new_number == target:
        # front 삭제하여 추출한 값이 목표값과 같은 경우
            return cnt
            # 연산 횟수 반환
        for i in range(4):
        # 4가지 연산 순회하는 for문
            ans = calculation(new_number, i)
            # 연산의 중간 결과
            if 0 <= ans <= 1000000 and not visited[ans]:
            # 연산의 중간 결과도 항상 백만 이하의 자연수 (-1 or -10 유의)
            # 연산의 중간 결과를 방문하지 않은 경우
                visited[ans] = cnt + 1
                # 연산 횟수를 방문배열에 추가
                queue.append(ans)
                # 연산 중간 결과 rear 삽입

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 자연수 N에 몇 번의 연산을 통해 다른 자연수 M

    visited = [0]* 1000001
    # 사용할 수 있는 연산이 +1, -1, *2, -10 네 가지(곱셈 덧셈 뺄셈)
    # 연산의 중간 결과도 항상 백만 이하의 자연수 (-1 or -10 유의)

    # result = 9999999
    # 최소 몇 번의 연산을 거쳐야 하는지

    print("#{} {}".format(tc, DFS(N, M)-1))
    # 방문배열 표시를 위해 처음 값을 1로 설정하고 연산할 때마다 1 추가