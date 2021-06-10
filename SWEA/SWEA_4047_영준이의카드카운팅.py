import sys
sys.stdin = open("4047.txt", "r")

T = int(input())
for tc in range(1, T+1):
    S = input()
    # str 한 줄 읽기 (input())
    # 카드에 대한 정보 S (1 ≤ |S| ≤ 1000)
    # T는 카드의 무늬(S, D, H, C)이며 XY는 카드의 숫자 (01 ~ 13)

    info = []
    # 빈 리스트 초기값
    for i in range(len(S)):
        if not i%3:
        # 인덱스가 3으로 나누어 떨어졌을 때
            info.append(S[i:i+3])
            # S는 각각 3자리로 표현되는 카드들의 정보(TXY)
            # T는 카드의 무늬(S, D, H, C)이며 XY는 카드의 숫자 (01 ~ 13)
            # 3글자씩 슬라이싱한 str을 빈 리스트에 추가

    s = d = h = c = 13
    #  “한 덱” 스페이드, 다이아몬드, 하트, 클로버 무늬 별 각각 13장씩 총 52장의 카드
    # 카드 장수 초기값

    if len(set(info)) != len(S)//3:
    # 이미 겹치는 카드가 있다면
    # info의 리스트에서 중복 제거(set()) 후의 길이가 줄어들어
    # len(s)을 3글자씩 나눈 TXY의 개수와 일치하지 않는다면
        print("#{} {}".format(tc, 'ERROR'))
        # 문자열 “ERROR” (쌍따옴표는 출력하지 않는다)를 출력

    else:
        for i in info:
        # info 리스트의 문자열 순회하는 for문
            if i[0] == 'S':
            # str 문자열의 첫번째 인덱스 부분이 카드의 종류를 의미([0])
            # 문자열 S와 같은 경우 ('S')
                s -= 1
            elif i[0] == 'D':
                d -= 1
            elif i[0] == 'H':
                h -= 1
            else:
                c -= 1
                # 지금 무늬 별로(S, D, H, C 순서로) 몇 장의 카드가 부족
        print("#{} {} {} {} {}".format(tc, s, d, h, c))
        # for문과 동등한 위치
        # else와 동등한 위치에 존재하면 에러의 경우에도 출력