'''
2 7 4 3 6
8 5 8 3 2
2 2 3 6 9
5 9 2 5 7
3 6 2 9 4

11 10 8 4 7
15 11 17 9 12
9 11 10 10 12
9 21 11 10 7
5 10 11 16 8
'''

arr = [list(map(int, input().split())) for _ in range(5)]
# 5X5 배열 for문으로 분리
# 2차원 리스트

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# 상하좌우
# drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]

final_lst = []
for r in range(5):
# r 0~4로 증가 for문
    for c in range(5):
    # c 0~4로 증가 for문
        # print(r, c)
        # 행렬 위치 인덱스 출력
        my_sum = 0
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr < 0 or nr >= len(arr) or nc < 0 or nc >= len(arr):
                continue
            # 초기값 가운데 위치 설정 [1, 1]가 아니라면 범위를 벗어나는 경우 존재
            # if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
            # if 0 <= nr < N and 0 <= nc < N:
            # N은 len(arr)
            # 범위에 속하지 않을 때 실행하지 않고 넘긴다
            else:
                if arr[nr][nc] - arr[r][c] < 0:
                # 음수인 경우 절대값 씌우고 합계
                    my_sum += (arr[r][c] - arr[nr][nc])
                else:
                # 양수인 경우 그대로 합계
                    my_sum += (arr[nr][nc] - arr[r][c])
        final_lst.append(my_sum)

for i in range(len(final_lst)):
    if (i+1) % 5 == 0:
        print(final_lst[i])
    else:
        print(final_lst[i], end=' ')