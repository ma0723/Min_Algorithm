import sys
sys.stdin = open("3499.txt", "r")

T = int(input())
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
for tc in range(1, T+1):
    N = int(input())
    # 각 테스트 케이스의 첫 번째 줄에는 자연수 N(1 ≤ N ≤ 1,000)
    # 카드 장수
    card = list(input().split())
    # 두 번째 줄에는 덱에 카드가 놓인 순서대로 N개의 카드 이름이 공백으로 구분되어 주어진다.
    # 카드의 이름은 알파벳 대문자와 ‘-’만으로 이루어져 있으며, 길이는 80이하이다

    first = []
    second = []
    final = []

    if N%2:
    # N이 홀수이면, 교대로 놓을 때 먼저 놓는 쪽에 한 장이 더 들어가게 하면 된다 (N//2+1, N//2)
        first = card[:N//2+1]
        second = card[N//2+1:]
        for i in range(N // 2 + 1):
            final.append(first[i])
            if i == N // 2:
                pass
            else:
                final.append(second[i])
    else:
    # 카드 덱을 정확히 절반으로 나누고 나눈 것들에서 교대로 카드를 뽑아 새로운 덱
        first = card[:N//2]
        second = card[N//2:]
        for i in range(N//2):
            final.append(first[i])
            final.append(second[i])

    print("#{}".format(tc), end=' ')
    for i in final:
        print(i, end=' ')
    print()
    # N개의 카드가 있는 덱이 주어질 때 이를 퍼펙트 셔플하면 어떤 순서가 되는지 출력하는 프로그램
