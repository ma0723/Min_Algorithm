import sys
sys.stdin = open("4834.txt", "r")
# 카운팅 정렬

T = int(input())
for tc in range(1, T + 1):
# test case 수 만큼 반복

    n = int(input())
    # 테스트케이스의 첫 줄에 카드 장수 N
    card = input()
    card = [int(_) for _ in card]
    # N개의 숫자 ai가 여백없이
    # 여백 없는 str을 for문으로 꺼낼 때마다 정수형 변환(int)
    # 각 숫자의 카드를 담을 상자 list 생성([])
    cnt_lst = [0] * 10
    # 0 ≤ ai ≤ 9 이므로  card list는 0부터 9까지 10개
    # card의 번호대로 담을 상자 list 생성([0]*10)
    # 카운팅 정렬

    for i in range(n):
    # 카드 장수 n개 0, 1, ... , n-1까지
        cnt_lst[card[i]] += 1
        # card[i]는 카드의 장수 개수 n개 만큼 index가 붙어서 card list에서 각 숫자 카드를 의미
        # cnt_list[]는 10개의 0이 적힌 상자 중 각 숫자 카드랑 동일한 숫자의 index에 1을 추가하여 개수 산정
        # 카운팅 정렬

    max_cnt, max_num = 0, 0
    # 가장 많은 숫자 카드의 개수, 가장 많은 숫자 카드의 종류
    for i in range(len(cnt_lst) - 1, -1, -1):
        # 가장 뒤의 index부터 0 index까지
        if cnt_lst[i] > max_cnt:
            max_cnt = cnt_lst[i]
            # 가장 많은 숫자 카드의 개수(cnt_lst[i])
            max_num = i
            # 가장 많은 숫자 카드의 종류(cnt_lst의 index 번호와 일치해서 i)

    print('#{} {} {}'.format(tc, max_num, max_cnt))