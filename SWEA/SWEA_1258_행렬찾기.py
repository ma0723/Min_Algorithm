import sys
sys.stdin = open("1258.txt", "r")

# 화학 물질 용기 n2개가 n x n으로 배열
# 빈 용기에 해당하는 원소는 ‘0’으로 저장
# 화학 물질이 들어 있는 용기에 해당하는 용기는 화학 물질의 종류에 따라 ‘1’에서 ‘9’사이의 정수를 저장

def search(r, c):
# 사각형의 크기를 찾는 함수
    r_cnt = 0
    c_cnt = 0
    for i in range(r, N):
    # 행의 길이
        if arr[i][c] != 0:
            r_cnt += 1
        else:
            break
    for i in range(c, N):
    # 행의 길이
        if arr[r][i] != 0:
            c_cnt += 1
        else:
            break
    ans.append([r_cnt, c_cnt, r_cnt*c_cnt])
    init(r, c, r_cnt, c_cnt)

def init(r, c, r_cnt, c_cnt):
# 0으로 용기 행렬 초기화
    for i in range(r, r+r_cnt):
        for j in range(c, c+c_cnt):
            arr[i][j] = 0

def counting_sort(idx):
# 카운팅 정렬(행렬 인덱스)
# 두번째 열인덱스 카운팅 정렬 후
# 첫번째 행인덱스 카운팅 정렬
    cnt = [0]*10001
    sort_ans = [0]*len(ans)
    #1 카운팅
    for i in range(len(ans)):
        cnt[ans[i][idx]] += 1
    #2 누적
    for i in range(1, len(cnt)):
        cnt[i] += cnt[i-1]
    #3 정렬 삽입
    for i in range(len(ans)-1, -1, -1):
        sort_ans[cnt[ans[i][idx]]-1] = ans[i]
        cnt[ans[i][idx]] -= 1
    return sort_ans

T = int(input())
# 테스트 케이스의 수 T
for tc in range(1, T+1):
    N = int(input())
    # 양의 정수인 n
    # n은 100 이하
    arr = [list(map(int, input().split())) for _ in range(N)]
    # n x n 행렬
    # 부분 행렬의 열의 개수는 서로 다르며 행렬의 행의 개수도 서로 다르다
    # 2개의 화학 물질이 담긴 용기들로 이루어진 사각형들 사이에는 빈 용기들이 있다(가로, 세로)
    # 대각선 상으로는 빈 용기가 없을 수도 있다

    ans = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                search(i, j)

    # 델타
    # 방문표시 (갔던 길 중복 방지)
    # 행렬의 길이

    # 정렬
    ans = counting_sort(0)
    # 행을 기준으로 정렬
    ans = counting_sort(2)
    # 행렬의 크기로 다시 한번 정렬
    # ans.append([r_cnt, c_cnt, r_cnt*c_cnt])의 인덱스 0과 2
    # ans.sort(key=lambda x:(x[0]*x[1], x[0]))
    # 행렬의 크기로 정렬하고 아니면 행의 크기로 정렬

    # 출력
    # 주어진 행렬에서 추출된 부분 행렬들을 개수와 그 뒤를 이어 행렬들의 행과 열의 크기를 출력
    # 크기는 행과 열을 곱한 값으로, 크기가 작은 순서대로 출력
    # 크기가 같을 경우 행이 작은 순으로 출력

    print("#{} {}".format(tc, len(ans)), end=' ')
    for i in range(len(ans)):
        print("{} {}".format(ans[i][0], ans[i][1]), end=' ')
    print()
    # 다음 문제를 위해 개행

T = int(input())
# 테스트 케이스의 수 T
for tc in range(1, T + 1):
    N = int(input())
    # 양의 정수인 n
    # n은 100 이하
    arr = [list(map(int, input().split())) for _ in range(N)]
    # n x n 행렬
    # 부분 행렬의 열의 개수는 서로 다르며 행렬의 행의 개수도 서로 다르다
    # 2개의 화학 물질이 담긴 용기들로 이루어진 사각형들 사이에는 빈 용기들이 있다(가로, 세로)
    # 대각선 상으로는 빈 용기가 없을 수도 있다

    ans = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                r, c = i, j
                # 다른 변수로 저장
                while r < N and arr[r][j] != 0:
                    r+= 1
                while c < N and arr[i][c] != 0:
                    c+= 1
                ans.append([r-i, c-j])
                # 폭발물의 길이 저장

                for a in range(i, r):
                    for b in range(j, c):
                        arr[a][b] = 0
                        # 폭발물 길이를 센 이후 빈 용기 0 처리

    ans.sort(key=lambda x: (x[0] * x[1], x[0]))
    # 크기 순서대로 작은 순서대로 정렬
    # 행 x[0] 열 x[1] 순서대로 정렬

    print("#{} {}".format(tc, len(ans)), end=' ')
    # 추출된 부분 행렬들을 개수
    for i in range(len(ans)):
        print("{} {}".format(ans[i][0], ans[i][1]), end=' ')
        # 행렬들의 행과 열의 크기를 출력
        # 크기는 행과 열을 곱한 값으로, 크기가 작은 순서대
    print()
    # 다음 문제를 위해 개행