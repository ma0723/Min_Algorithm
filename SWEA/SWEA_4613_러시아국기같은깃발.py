import sys
sys.stdin = open("4613.txt", "r")

# 깃발은 N행 M열로 나뉘어 있고, 각 칸은 흰색, 파란색, 빨간색 중 하나
# 위에서 몇 줄(한 줄 이상)은 모두 흰색으로 칠해져 있어야 한다.
# 다음 몇 줄(한 줄 이상)은 모두 파란색으로 칠해져 있어야 한다.
# 나머지 줄(한 줄 이상)은 모두 빨간색으로 칠해져 있어야 한다.
# 새로 칠해야 하는 칸의 개수의 최솟값

# def dfs(idx, color, total):
# # idx lst list의 행 인덱스
# # color color list의 인덱스
# # 1 ~ N-2 행의 색까지의 변화할 개수의 합
#     global result
#     # result 값 변경 global
#     # dfs를 이용하여 모든 경우의 수를 탐색
#     if result <= total:
#         return
#         # 가치지기
#     if idx == N-1:
#     # idx가 N-2까지 진행된 후 재귀 호출할 경우
#         result = total
#         # 결과 더하기
#         return
#         # 호출한 곳으로 return
#     #다음색상까지, 넘어온게 흰색이라면  흰색, 파랑만
#     #인덱스때문에 최댓값은 3으로 설정
#     for i in range(color, 3):
#     # color 인덱스 i(0, 1, 2)
#         temp = 0
#         # 초기값 0
#         if idx >= N-2 and i == 0:
#         # lst 마지막줄 바로 위까지 오기 전에
#         # lst 컬러가 흰색이라면
#             continue
#             # 다음으로 넘어가기
#         for j in lst[idx]:
#         # 열 순회
#             if j != color[i]:
#             # 색상이 다른 경우
#             temp += 1
#             # 임시 합 1씩 증가
#         dfs(idx+1, i, total + temp)
#         # 재귀

# T = int(input())
# # 테스트 케이스의 수 T
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     # 두 정수 N,M(3≤N,M≤50)이 공백으로 구분
#     lst = [[i for i in input()] for _ in range(N)]
#     # N개의 줄(행)에는 M개의 문자(열)로 이루어진 문자열
#     # ‘W’는 흰색, ‘B’는 파란색, ‘R’은 빨간색을 의미

#     # 러시아 깃발은 3색
#     color = ['W', 'B', 'R']
    
#     result = 0
#     # 초기값 설정
#     for i in range(M):
#     # 열 순회
#         if lst[0][i] != 'W':
#         # 가장 위쪽 행[0] W
#             result += 1
#         if lst[N-1][i] != 'R':
#         # 가장 아래쪽 행[N-1] R
#             result += 1

#     # 가운데 행 바로 직전 위쪽 아래쪽 행의 색 고려 W B R
#     # 가운데 행 글자수가 가장 많은 것을 고려해서 전환 W B R
#     dfs(1, 0, 0)

#     print("#{} {}".format(tc, result))

# 재귀
def perm(idx, total):
    global ans
    if total > N:
        return
        # 가지치기
    if idx == 3:
        if total == N:
            cnt = 0
            st = sel[0]
            st2 = st + sel[1]

            for i in flag[:st]:
            # 흰색 칠하기
                for j in i:
                    if j!='W':
                        cnt += 1
            for i in flag[st:st2]:
            # 파란색 칠하기
                for j in i:
                    if j!='B':
                        cnt += 1
            for i in flag[st2:]:
            # 빨간간색 칠하기
               for j in i:
                    if j!='R':
                        cnt += 1
            if ans > cnt:
                ans = cnt
        return

    for i in range(1, N-1):
        sel[idx] = i
        perm(idx+1, total + i)

T = int(input())
# 테스트 케이스의 수 T
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 두 정수 N,M(3≤N,M≤50)이 공백으로 구분
    flag = [list(input()) for _ in range(N)]
    # N개의 줄(행)에는 M개의 문자(열)로 이루어진 문자열
    # ‘W’는 흰색, ‘B’는 파란색, ‘R’은 빨간색을 의미
    sel = [0]*3
    # 색깔별 숫자
    ans = 99999999

    perm(0,0)

    print("#{} {}".format(tc, ans))

# # for문
# T = int(input())
# # 테스트 케이스의 수 T
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     # 두 정수 N,M(3≤N,M≤50)이 공백으로 구분
#     flag = [input() for _ in range(N)]
#     # N개의 줄(행)에는 M개의 문자(열)로 이루어진 문자열
#     # ‘W’는 흰색, ‘B’는 파란색, ‘R’은 빨간색을 의미

#     W = [0]*N
#     B = [0]*N
#     R = [0]*N

#     # 행을 보면서 나와 다른 색 개수 카운팅
#     for i in range(N):
#         for j in range(M):
#             if flag[i][j] != 'W':
#                 W[i] += 1
#             if flag[i][j] != 'B':
#                 B[i] += 1
#             if flag[i][j] != 'R':
#                 R[i] += 1

#     # 누적
#     for i in range(1, N):
#         W[i] += W[i - 1]
#         B[i] += B[i - 1]
#         R[i] += R[i - 1]

#     ans = 99999999

#     for i in range(N-2):
#     # 마지막 줄은 고정(N-2)
#         for j in range(i+1, N-1):
#             w_cnt = W[i]
#             b_cnt = B[j] - B[i]
#             r_cnt = R[N-1] - R[j]

#             if ans > w_cnt + b_cnt + r_cnt:
#                 ans = w_cnt + b_cnt + r_cnt

#     print("#{} {}".format(tc, ans))