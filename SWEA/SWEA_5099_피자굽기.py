import sys
sys.stdin  = open("5099.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N개의 피자를 동시에 구울 수 있는 화덕
    # 1번부터 M번까지 M개의 피자를 순서대로 화덕
    lst = list(map(int, input().split()))
    # M개의 피자에 뿌려진 치즈의 양을 나타내는 Ci
    q = []
    # 큐 생성(화덕)
    for i in range(N):
        q.append([lst[i], i])
        # 치즈양, 피자번호(인덱스0 유의, i+1로 가능) list rear 삽입
        # 피자 N개 삽입

    i = 0
    # 변수 초기값 0
    while len(q)!=1:
    # 가장 마지막까지 남아있는 피자 번호를 알아내는 프로그램
    # q에 피자가 1개 남아있을 때 반복 종료
        q[0][0] //= 2
        # 화덕을 한 바퀴 돌 때 녹지않은 치즈의 양은 반으로 줄어든다
        # [0] 첫번째로 넣은 피자의 [0] 치즈양
        # 피자는 1번위치에서 넣거나 뺄 수 있다
        if q[0][0] == 0:
        # 치즈가 모두 녹아 0이 되면
        # 피자는 1번위치에서 넣거나 뺄 수 있다
            if N+i < M:
            # 화덕의 용량이 넣어야 하는 이미 넣은 피자 개수(N+i)보다 작으면
                q.pop(0)
                # 화덕에서 꺼내고
                # queue front 삭제
                q.append([lst[N+i], N+i])
                # 바로 그 자리에 남은 피자를 순서대로 넣는다
                # queue rear 삽입
                # [lst[N-1], N-1]이 마지막으로 넣은 피자의 치즈양과 피자번호
                i+=1
                # 변수 i 1씩 증가
            elif N+i >= M:
            # 화덕의 용량이 넣어야 하는 피자 개수(N+i)보다 크거나 같으면
                q.pop(0)
                # 화덕에서 꺼내고
                # queue front 삭제
        else:
        # 치즈가 모두 녹아내리지 않은 경우
            q.append(q.pop(0))
            # 천천히 회전 순서 변경 가능
            # queue front 삭제
            # queue rear 삽입

    print("#{} {}".format(tc, q[0][1]+1))
    # [0] 큐에 남은 가장 마지막 피자의 [1] 피자번호 (인덱스+1)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N개의 피자를 동시에 구울 수 있는 화덕
    # 1번부터 M번까지 M개의 피자를 순서대로 화덕
    pizza = list(map(int, input().split()))
    # M개의 피자에 뿌려진 치즈의 양을 나타내는 Ci
    firepot = []
    # 큐 생성(화덕)

    for i in range(N):
        firepot.append((i+1, pizza[i]))
        # 피자번호(인덱스0부터 유의) 치즈양
        # 큐 삽입

    # N번부터 피자 넣기
    next_pizza = N
    last_pizza = -1

    while firepot:
        num, cheese = firepot.pop(0)
        # 큐 제거

        cheese //= 2
        last_pizza = num

        if cheese:
            firepot.append((num, cheese))
            # 큐 추가
        else:
        # 치즈가 녹아내린 경우
            if next_pizza < M:
            # 다음 피자의 번호가 M개보다 작은 경우
                firepot.append(next_pizza+1, pizza[next_pizza])
                # N번 이후 피자 삽입
                next_pizza += 1
                # 다음피자 번호 증가

    print("#{} {}".format(tc, last_pizza))
