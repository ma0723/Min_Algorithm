import sys
sys.stdin = open("1979.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) + [0] for _ in range(N)]
    # 우측 0의 가상 벽 추가 (+ [0])
    lst.append([0] * (N + 1))
    # 하측 0의 가상 벽 추가 (lst.append([0]*(N+1)))
    print(*lst)
    # N X N 크기의 단어 퍼즐

    # N은 5 이상 15 이하의 정수
    # K는 2 이상 N 이하의 정수

#     ans = 0
#
#     for i in range(N):
#         cnt = 0
#         for j in range(N):
#             if lst[i][j] == 1:
#                 cnt += 1
#             if lst[i][j] == 0 or j==N-1:
#             # 벽을 만났을 때 개수
#             # 변화하는 행의 인덱스가 마지막 인덱스일 떄(j==N-1)
#                 if cnt == M:
#                     ans += 1
#                 cnt = 0
#                 # 초기화
#         for j in range(N):
#             if lst[j][i] == 1:
#                 cnt += 1
#             if lst[j][i] == 0 or j==N-1:
#             # 벽을 만났을 때 개수
#             # 변화하는 행의 인덱스가 마지막 인덱스일 떄(j==N-1)
#                 if cnt == M:
#                     ans += 1
#                 cnt = 0
#                 # 초기화
#     # 연속된 0의 개수 == M
#     # 특정 길이 M를 갖는 단어가 들어갈 수 있는 자리의 수를 출력
#     print("#{} {}".format(tc, ans))
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     lst = [list(map(int, input().split())) for _ in range(N)]
#     lst.append([0]*(N+1))
#     # 오른쪽과 아래쪽에 모두 0의 벽을 추가하면
#     # 벽이라서 갈 수 없는 것을 고려
#     # i for문(즉 고정된 변수는 그대로 N)
#     # j for문(즉 변화하는 변수는 N+1)
#     ans = 0
#     for i in range(N):
#         cnt = 0
#         for j in range(N+1):
#             if lst[i][j]:
#                 cnt += 1
#             else:
#                 if cnt == M:
#                     ans += 1
#                 cnt = 0
#         for j in range(N+1):
#             if lst[j][i]:
#                 cnt += 1
#             else:
#                 if cnt == M:
#                     ans += 1
#                 cnt = 0
#     print("#{} {}".format(tc, ans))