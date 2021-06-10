import sys
sys.stdin = open("1970.txt", "r")

T = int(input())
for tc in range(1, T + 1):

    N = input()
    # 거스름돈 str
    N = int(N[:len(N) - 1] + '0')
    # input의 N이 0으로 끝나지 않는 경우를 위해 마지막 자리수 슬라이싱(N[:len(N)-1])
    # str에 str 0을 추가한 후 정수형 전환 int()

    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    # 거스름돈의 종류 리스트
    result = [0] * len(money)
    # 거스름돈의 개수
    # 카운팅 정렬

    i = 0
    # 가장 큰 거스름돈 인덱스 초기값
    # money[0]은 가장 큰 거스름돈인 50000 초기값
    while i < len(money) or N > 0:
        # 거스름 돈이 0이하면 종료
        # 인덱스가 거스름돈의 리스트 인덱스를 벗어나면 종료
        if N // money[i] != 0:
            # 거스름돈으로 나눈 몫이 0이 아니라면
            result[i] += N // money[i]
            # 거스름돈으로 나눈 몫이 개수로 카운팅 정렬 값으로 추가
            N = N % money[i]
            # 거스름돈으로 나눈 나머지가 남은 금액 갱신
        else:
            # 거스름돈으로 나눈 몫이 0이라면
            i += 1
            # 다음으로 큰 거스름돈으로 이동하기 위해 인덱스 추가

    print('#{} '.format(tc))
    # 개행
    print(*result)
    # *은 리스트의 모든 값을 행렬처럼 출력

# 탐욕 알고리즘
# 큰 단위의 돈부터 작은 단위의 돈까지 차례로 주어진 거스름돈에서 빼준다
coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())
for tc in range(1, T + 1):
    print('#{}'.format(tc))

    change = int(input())
    result = []
    # 빈 리스트 초기값

    for coin in coins:
        # 가장 큰 거스름돈부터 순회
        mok = change // coin
        result.append(mok)
        # 거스름돈으로 나눈 몫(개수)을 추가
        change -= mok * coin
        # 개수*거스름돈를 빼면서 남은 금액 갱신

    print(' '.join(list(map(str, result))))
    # 문자열 전환 후 (map(str, result))
    # 리스트로 생성 (list())
    # 문자열로 공백 1칸을 띄어쓰고 출력 (' '.join())