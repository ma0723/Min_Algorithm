import sys
sys.stdin = open("5789.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    # 두 정수 N, Q (1 ≤ N, Q ≤ 103)가 공백

    box = [0]*N
    # 1번부터 N번까지 N개의 상자
    # 각 상자에는 숫자를 새길 수 있는데 처음에는 모두 0
    # 다음 Q회 동안 일정 범위의 연속한 상자를 동일한 숫자로 변경

    index = [list(map(int, input().split())) for _ in range(Q)]
    
    # Q개의 줄의 i번째 줄에는 Li, Ri (1 ≤ Li ≤ Ri ≤ N)

    for i in range(Q):
    # Q회 동안 위의 작업을 순서대로 한 다음
        L = index[i][0]
        R = index[i][1]
        for j in range(L-1, R):
        # L번 상자부터 R번 상자까지의 값을
        # box의 인덱스는 L-1부터 R-1까지
            box[j] = i+1
            # i (1 ≤ i ≤ Q)번째 작업에 대해 값을 i로 변경
            # i for문은 index이므로 값은 1추가

    T = int(input())
    for tc in range(1, T + 1):
        N, Q = map(int, input().split())
        # 두 정수 N, Q (1 ≤ N, Q ≤ 103)가 공백

        box = [0] * N
        # 1번부터 N번까지 N개의 상자
        # 각 상자에는 숫자를 새길 수 있는데 처음에는 모두 0
        # 다음 Q회 동안 일정 범위의 연속한 상자를 동일한 숫자로 변경

        index = [list(map(int, input().split())) for _ in range(Q)]
        # Q개의 줄의 i번째 줄에는 Li, Ri (1 ≤ Li ≤ Ri ≤ N)

        for i in range(Q):
            # Q회 동안 위의 작업을 순서대로 한 다음
            L = index[i][0]
            R = index[i][1]
            for j in range(L - 1, R):
                # L번 상자부터 R번 상자까지의 값을
                # box의 인덱스는 L-1부터 R-1까지
                box[j] = i + 1
                # i (1 ≤ i ≤ Q)번째 작업에 대해 값을 i로 변경
                # i for문은 index이므로 값은 1추가

    print("#{}".format(tc), end=' ')
    for i in box:
        print(i, end=' ')
    print()
    # 다음 tc 개행