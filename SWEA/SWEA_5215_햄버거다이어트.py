import sys
sys.stdin = open("5215.txt", "r")

# 완전탐색
# 재귀
# 가지치기

def search(idx, score, cal):
    global result
    # 값 변경을 위해 global
    if cal > L:
    # 칼로리 누적합이 제한된 최고 칼로리를 넘어가면
        return
        # 재귀 호출
    if score > result:
        # 최고맛 점수보다 높다면
        result = score
        # 갱신
    if idx == N:
    # 마지막 인덱스
        return
        # 재귀 호출
    search(idx+1, score + score_lst[idx], cal+cal_lst[idx])
    # 재료 사용하는 경우
    search(idx+1, score, cal)
    # 재료 사용하지 않는 경우

# 여러 재료를 조합하였을 햄버거의 선호도는 조합된 재료들의 맛에 대한 점수의 합으로 결정
# 같은 재료를 여러 번 사용할 수 없다

T = int(input())
# 테스트 케이스의 수 T

for tc in range(1, T+1):
    N, L = map(int, input().split())
    # 재료의 수, 제한 칼로리를 나타내는 N, L가 공백으로 구분

    score_lst = []
    cal_lst = []
    for _ in range(N):
    # N개의 줄
        score, cal = map(int, input().split())
        # 점수와 칼로리를 나타내는 Ti, Ki가 공백으로 구분
        score_lst.append(score)
        cal_lst.append(cal)

    result = 0
    # 주어진 제한 칼로리 이하의 조합중에서 가장 맛에 대한 점수가 높은 햄버거의 점수

    search(0, 0, 0)

    print("#{} {}".format(tc, result))