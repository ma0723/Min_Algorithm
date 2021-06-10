import sys
sys.stdin = open("5432.txt", "r")

T = int(input())
for tc in range(1, T+1):
    iron = input()

    cnt = 0
    # 쇠막대기의 수
    ans = 0
    # 잘려지는 막대기의 수

    for i in range(len(iron)):
        if iron[i] == '(':
        # 열린 괄호이면
            cnt += 1
            # 쇠막대기 수 1개 증가
        else:
        # 닫힌 괄호이면
            cnt -= 1
            # 쇠막대기 1개 감소
            # 레이저라면 당연히 잘못 세어서 뺀다
            # 아니라면 쇠막대기 끝이라서 뺴는게 맞다
            if iron[i-1] == '(':
            # 레이저가 존재한다면
                ans += cnt
                # 지금까지 존재한 쇠막대기 개수만큼 반토막 나서 추가
            else:
            # 쇠막대기 끝이라면
                ans += 1
                # 잘려진 막대기 1개 증가
    print("#{} {}".format(tc, ans))

T = int(input())
for tc in range(1, T + 1):
    iron = input()
    s = []
    ans = 0

    for i in range(len(iron)):
        if iron[i] == '(':
            s.append('(')
        else:
            s.pop()
            # 인덱스 위치 제거
            # 아무것도 넣지 않으면 가장 뒷 인덱스 제거
            if iron[i-1] == '(':
                ans += len(s)
                # 레이저로 인해 이전의 모든 쇠막대기들이 잘린 경우
            else:
                ans += 1
                # 쇠막대기 끝의 경우
    print("#{} {}".format(tc, ans))

# swea1213 string 문자열 비교와 유사

