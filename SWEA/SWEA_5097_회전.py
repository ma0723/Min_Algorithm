import sys
sys.stdin  = open("5097.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    # 첫 줄에 N과 M이 주어지고
    num = list(map(int, input().split()))
    # 다음 줄에 10억 이하의 자연수 N개
    # 큐 리스트
    for i in range(M):
    # 맨 뒤로 보내는 작업을 M번 했을 때
        result = num.pop(0)
        # 맨 앞의 숫자 front 삭제
        num.append(result)
        # 맨 뒤로 rear 삽입

        # num.append(num.pop(0))

    print("#{} {}".format(tc, num[0]))
    # 수열의 맨 앞에 있는 숫자를 출력