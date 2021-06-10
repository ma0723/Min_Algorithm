import sys
sys.stdin = open("4839.txt", "r")

# 중간 페이지 c= int((l+r)/2)로 계산한다.
# 찾는 쪽 번호가 c와 같아지면 탐색을 끝낸다.
# 먼저 펼치는 사람이 이기는 게임
# 비긴 경우는 0을 출력

T = int(input())
for tc in range(1, T+1):
    P, a, b = map(int, input().split())

    l= 1
    r = P
    # 초기값 설정

    a_cnt = 0
    # 초기값 설정
    while l <= r:
        c = (l + r) // 2
        # 몫으로 나누어 정수형(//)
        if a == c:
            a_cnt += 1
            break
            # while문 종료
        elif a > c:
            a_cnt += 1
            l = c
            # 중앙값을 시작점(l)
        else:
            a_cnt += 1
            r = c
            # 중앙값을 종착점(r)

    l= 1
    r = P
    # 초기값 설정

    b_cnt = 0
    # 초기값 설정
    while l <= r:
        c = (l + r) // 2
        # 몫으로 나누어 정수형(//)
        if b == c:
            b_cnt += 1
            break
            # while문 종료
        elif b > c:
            b_cnt += 1
            l = c
            # 중앙값을 시작점(l)
        else:
            b_cnt += 1
            r = c
            # 중앙값을 종착점(r)

    if a_cnt < b_cnt:
    # B가 이진 검색 횟수가 더 많은 경우
        result = 'A'
    elif a_cnt > b_cnt:
    # A가 이진 검색 횟수가 더 많은 경우
        result = 'B'
    else:
    # 비기는 경우
        result = 0

    print("#{} {}".format(tc, result))

def find(total, p):
# total 전체 페이지
# p 찾으려는 페이지
    l = 0
    r = total
    c = int((l+r)/2)
    # 중간 페이지
    cnt = 1
    # 최소 1번은 c를 만들어서 초기값 1
    while c!=p:
    # 찾는 페이지가 아닐 동안 반복
        if c < p:
            l = c
        else:
            r = c
        cnt+= 1
        # 횟수 카운팅
        c = int((l+r)/2)
        # 중간값 갱신
    return cnt


T = int(input())
for tc in range(1, T+1):
    P, a, b = map(int, input().split())
    ra = find(P, a)
    rb = find(P, b)
    # 함수의 리턴값을 다른 변수에 저장

    if ra<rb:
        result = "A"
    elif ra>rb:
        result = "B"
    else:
        result = 0

    print("#{} {}".format(tc, result))

