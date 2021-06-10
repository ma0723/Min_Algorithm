import sys
sys.stdin = open("10726.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 정수 N, M 이 주어질 때

    ans = []
    # 10진수 -> 2진수
    while M > 0:
        ans.append(str(M % 2))
        # 나머지 (역순이므로 추후 슬라이싱 뒤집기)
        M //= 2
        # 몫
    ans = ans[::-1]
    # 역순
    
    if len(ans) < N:
    # 이진수 표기 후 길이가 N비트보다 작을 때
        ans = [0]*(N-len(ans)) + ans    
        # 길이 차이만큼 앞부분에 0 표기

    cnt = 0
    # 개수
    for i in range(len(ans)-1, len(ans)-(N+1), -1):
    # 마지막 비트부터 마지막 N비트까지 순회
        if ans[i] == '1':
            cnt += 1
    if cnt == N:
    # 모든 N비트가 1인 경우
        result = 'ON'
    else:
    # 모든 N비트가 1이 아닌 경우 
        result = 'OFF'

    print("#{} {}".format(tc, result))
    # M의 이진수 표현의 마지막 N 비트가 모두 1로 켜져 있는지 아닌지를 판별하여 출력