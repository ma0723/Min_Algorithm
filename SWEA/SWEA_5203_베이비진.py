import sys
sys.stdin = open("5203.txt", "r")

def counting(player):
# 카운팅
    cards = [0]*12
    for card in player:
    # 숫자를 분리
        cards[card] += 1
        # 카드 숫자 인덱스에 0값을 카드 장수 1씩 추가
    return cards

def babygin(i, card):
    tri = 0
    run = 0
    while i < 10:
        if card[i] >= 3:
        # 트리플
        # 카운팅 정렬은 해당하는 카드 번호와 일치하는 인덱스에 카드 개수를 값으로 입력
            card[i] -= 3
            # 트리플렛 3장의 카드 제거
            tri += 1
            # 초기값 0에서 추가
        if card[i] >= 1 and card[i + 1] >= 1 and card[i + 2] >= 1:
        # 런
        # 세 장의 연속된 인덱스의 카드가 1장 이상씩 존재한다면 런
            card[i] -= 1
            card[i + 1] -= 1
            card[i + 2] -= 1
            # 런 각 카드 제거
            run += 1
            # 초기값 0에서 추가
        i += 1
    return tri + run
    # while문 종료 후
    # i == 9까지 확인한 후

T = int(input())
for tc in range(1, T+1):
    players = list(map(int, input().split()))
    player1 = []
    player2 = []
    ans1 = 0
    ans2 = 0
    for idx, card in enumerate(players):
        if idx%2==0:
        # 홀수번째 카드 (인덱스 + 1) 첫번째 플레이어
            player1.append(card)
            ans1 = babygin(0, counting(player1))
        else:
        # 짝수번째 카드 (인덱스 + 1) 두번째 플레이어
            player2.append(card)
            ans2 = babygin(0, counting(player2))
        if ans1 > ans2:
        # 6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자
            print("#{} {}".format(tc, 1))
            break
            # for문 카드 분배 순회 종료
        elif ans1 < ans2:
        # 6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자
            print("#{} {}".format(tc, 2))
            break
            # for문 카드 분배 순회 종료
    else:
    # for문 카드 분배 순회를 한 후에도 ans1=ans2=0 무승부
        print("#{} {}".format(tc, 0))
        # 무승부인 경우 0을 출력