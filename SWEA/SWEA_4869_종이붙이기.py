import sys
sys.stdin = open("4869.txt", "r")

def FindCase(x):
# x == 현재 위치
    if x > N:
    # 넣으려는 값(20*x)이 주어진 너비(20*N)보다 크다면
        return 0
        # 넣으려는 값(20*x)의 사각형이 들어가는 경우의 수는 0개
    elif x == N:
    # 넣으려는 값(20*x)이 주어진 너비(20*N)와 같다면
        return 1
        # 경우의 수 1개
    return FindCase(x + 10) + FindCase(x + 20) * 2
    # 넣으려는 값(20*x)이 주어진 너비(20*N)보다 작은 경우
    # x=0부터 시작하여
    # FindCase(10)
    # FindCase(20)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 10≤N≤300, N은 10의 배수
    # 가로x세로 길이가 10x20, 20x20인 직사각형 종이
    # 20xN 크기의 직사각형을 테이프로 표시하고, 이 안에 준비한 종이를 빈틈없이 붙이는 방법

    print('#{} {}'.format(tc, FindCase(0)))
    # 종이를 붙이는 모든 경우를 찾으려면
    # 테이프로 만든 표시한 영역을 몇 개나 만들어야 되는지

# 20*10 1개 : 10 1개 20 0개
# 20*20 1개 : 10 2개 20 0개 / 10 2개 20 0개 / 10 0개 20 1개
# 20*30 1개 : 10 3개 20 0개 / 10 3개 20 0개 / 10 1개 20 1개
#             10 3개 20 0개 / 10 1개 20 1개
# 20*40 1개 : 10 4개 20 0개 / 10 4개 20 0개 / 10 2개 20 1개 / 10 4개 20 0개 / 10 2개 20 1개
#             10 4개 20 0개 / 10 4개 20 0개 / 10 2개 20 1개
#             10 2개 20 1개 / 10 2개 20 1개 / 10 0개 20 2개
# 2*f(n-2)는 현 너비에서 2칸을 제외하고 붙일 경우 ||의 2개의 막대기가 채워지는 경우 외에 =과 ㅁ가 추가되는 경우 2가지
# f(n-1)는 현 너비에서 1칸을 제외하고 |를 한 번 더 붙인다

# 10으로 나눈 후 재귀
def f(n):
# n :  종이의 너비
    if n == 1 :
    # f(1) = 1
        return 1
    if n == 2 :
    # f(2) = 3
        return 3
    return f(n-1) + 2*f(n-2)
    # f(n-1) 현 너비에서 1칸을 제외하고 종이를 붙일 수 있는 경우의 수
    # f(n-1) 현 너비에서 2칸을 제외하고 종이를 붙일 수 있는 경우의 수
    # f(3) = f(2) + 2*f(1)
    # 다이나믹 프로그래밍 DP로 메모리 용량 줄이기

T = int(input())
for tc in range(1,T+1):
    N = int(input()) // 10
    # 10의 배수이므로 나눈다
    print("#{} {}".format(tc, f(N)))


# dp 재귀
T = int(input())

# 모든 N에 대한 경우의 수를 계산해놓기
l = [1,1]
# 0칸일때 1, 1칸일때 1, 초기값
for i in range(2,31):
# 문제에서 n = 30
    l.append(l[i-1] + 2 *l[i-2])
    # 인덱스에 따라 값을 추가

for tc in range(1,T+1):
    N = int(input()) // 10
    print("#{} {}".format(tc, l[N]))