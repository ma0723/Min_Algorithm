import sys
sys.stdin = open("1859.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 자연수 N(2 ≤ N ≤ 1,000,000)
    price = list(map(int, input().split()))
    # 각 날의 매매가를 나타내는 N개의 자연수들이 공백
    # 각 날의 매매가는 10,000이하
    # 판매는 얼마든지 할 수 있다

    max = price[len(price) - 1]
    # 가장 마지막 날의 가격을 최대값의 초기값
    profit = 0
    # 이익 초기값
    for i in range(len(price)-1, -1, -1):
    # 역순으로 진행
    # 뒷날부터 가격을 순회하면서 사재기할 주기(각 주기의 최대값 기준 끊기) 갱신
        if price[i] < max:
        # 가장 뒷 날의 가격보다 오늘의 가격이 작다면
            profit += max - price[i]
            # 구매
            # 이익 = 판매하는 날의 가격 - 구매한 날의 가격
        else:
        # 현재 저장된 가장 높은 가격보다 오늘의 가격이 높다면
            max = price[i]
            # 사재기할 주기(각 주기의 최대값 기준 끊기) 갱신
    print("#{} {}".format(tc, profit))

    # 하루에 최대 1만큼 구입
    # 매매가가 1, 2, 3 이라면 처음 두 날에 원료를 구매하여 마지막 날에 팔면 3의 이익(2, 1)
    # 1번째 케이스는 아무 것도 사지 않는 것이 최대 이익
    # 2번째 케이스는 1,2일에 각각 한 개씩 사서 세 번째 날에 두 개를 팔면 10의 이익(6, 4)


