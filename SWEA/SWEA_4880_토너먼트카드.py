import sys
sys.stdin = open("4880.txt", "r")

# 1번부터 N번까지 N명의 학생이 N장의 카드를 나눠 갖는다.
# 전체를 두 개의 그룹으로 나누고, 그룹의 승자끼리 카드를 비교해서 이긴 사람이 최종 승자
# 그룹의 승자는 그룹 내부를 다시 두 그룹으로 나눠 뽑는데
# 두 그룹이 각각 1명이 되면 양 쪽의 카드를 비교해 승자를 가리고, 다시 더 큰 그룹의 승자를 뽑는 방식
# 숫자 1은 가위, 2는 바위, 3은 보를 나타낸다.
# 만약 같은 카드인 경우 편의상 번호가 작은 쪽을 승자로 하고, 처음 선택한 카드는 바꾸지 않는다.

# 분할 정복
def find(l, r):
# 카드가 한 장일 때까지 나누기 위한 재귀 호출
    if l==r:
    # 카드가 한 장인 경우
        return l
        # 재귀 호출 종료
        # 각 카드의 인덱스 호출

    # 팀 나누기
    result1 = find(l, (l + r)//2)
    # 13 f(1, 2)
    # f(1, 1) 1 return f(2, 2) 2 return
    # card[1] card[2]
    result2 = find((l + r) // 2+1, r)
    # 21 f(3, 4)
    # f(3, 3) 3 return f(4, 4) 4 return
    # card[3] card[4]

    # 게임 진행
    if card[result1] == card[result2]:
    # 비긴 경우
        return result1
        # 왼쪽 카드(숫자가 작은 카드) 승
    else:
        # 가위1 바위2 보3
        if card[result1] == 1 and card[result2] == 2:
            return result2
        elif card[result1] == 1 and card[result2] == 3:
            return result1
        elif card[result1] == 2 and card[result2] == 1:
            return result1
        elif card[result1] == 2 and card[result2] == 3:
            return result2
        elif card[result1] == 3 and card[result2] == 1:
            return result2
        elif card[result1] == 3 and card[result2] == 2:
            return result1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 인원수 N
    card = [0] + list(map(int, input().split()))
    # N명이 고른 카드가 번호순으로 주어진다. 4≤N≤100
    # 1번째 카드 인덱스와 순서를 맞추기 위해 [0] 추가
    print("#{} {}".format(tc,find(1, N)))

    # team1 = lst[:N//2]
    # team2 = lst[N//2:]