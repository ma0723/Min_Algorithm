import sys
sys.stdin = open("1244.txt", "r")

def dfs(cnt):
    global result
    # result 값 변경
    if not cnt:
    # 횟수가 모두 차감되어 cnt=0인 경우
        temp = int(''.join(numbers))
        # 숫자 str을 join한 뒤 정수형 전환
        # 숫자판의 위치에 부여된 가중치에 의해 상금이 계산
        # 오른쪽 끝에서부터 1원이고 왼쪽으로 한자리씩 갈수록 10의 배수
        if result < temp:
        # 최대값 갱신
        # 교환 후 받을 수 있는 가장 큰 금액
            result = temp
        return
        # 가지치기 (result >= temp)
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
        # 인덱스 i의 다음 위치부터 순회하는 2중 for문
            numbers[i], numbers[j] = numbers[j], numbers[i]
            # 위치 교환
            temp_key = ''.join(numbers)
            # 숫자 str을 join해야 나열 가능
            if visited.get((temp_key, cnt - 1), 1):
            # .get(key, value) (교환 후 숫자, 교환 횟수 차수)를 key로 가진 dictionary 값을 1 혹은 0
            #1 key값이 없는 경우 빈 dictionary에 key와 value를 동시에 할당 (방문하지 않은 경우 1)
            #2 key값이 있는 경우 key에 해당하는 value 호출 (방문한 경우 0)
            # 같은 숫자여도 다른 회차면 분리(교환 횟수 차수를 고려해야 동일한 위치의 교환이 중복되어도 된다는 조건 충족)
            # 같은 숫자여도 같은 회차면 가지치기(재귀와 for문)
                visited[(temp_key, cnt - 1)] = 0
                # (교환 후 숫자, 교환 횟수 차수)를 key로 가진 경우가 .get()으로 이미 존재하여 dictionary 값 0
                # 방문한 경우
                dfs(cnt - 1)
                # 재귀 (교환 횟수 1번 차감)
            numbers[i], numbers[j] = numbers[j], numbers[i]
            # 위치 교환 원상복귀

T = int(input())
for tc in range(1, T+1):
    numbers, change_cnt = input().split()
    # 숫자판의 정보와 교환 횟수
    # 정수형 숫자로 주어지고 최대 자릿수는 6자리이며, 최대 교환 횟수는 10번
    numbers = list(numbers)
    # 각 숫자 list 값으로 분리
    change_cnt = int(change_cnt)
    # 카드 교환 횟수
    result = 0
    # 결과 global 교환 후 받을 수 있는 가장 큰 금액
    visited = {}
    # 가지치기 딕셔너리
    dfs(change_cnt)
    # 완전 탐색
    print("#{} {}".format(tc, result))

def back_track(now):
    # 중복 체크
    case = ''.join(cards)
    if case in visited[now]:
    # 있으면 진행 X
        return
    # 없는 경우에 케이스 추가하고 진행
    visited[now].add(case)

    if now == count:
        global result
        result = max(result, int(case))
    else:
        for i in range(len_cards - 1):
            for j in range(i + 1, len_cards):
                # 다음 케이스를 위해 자리 변경
                # [3, 2, 8, 8, 8]   =>  [3, 2, 8, 8, 8]
                # [2, 3, 8 ,8 ,8]   =>  [8, 2, 3, 8, 8]
                cards[i], cards[j] = cards[j], cards[i]
                # 재귀 호출 (현재까지 바꾼 횟수 + 1)
                back_track(now + 1)
                # 원상 복구
                # [2, 3, 8 ,8 ,8]
                # [3, 2, 8, 8, 8]
                cards[i], cards[j] = cards[j], cards[i]

T = int(input())

for tc in range(1, T + 1):
    data = input().split()
    cards = list(data[0])
    # ex. [3, 2, 8, 8, 8]
    count = int(data[1])
    # ex. 2
    len_cards = len(cards)
    visited = [set() for _ in range(count + 1)]
    result = 0
    back_track(0)
    print('#{} {}'.format(tc, result))

