from itertools import permutations
# from itertools import combinations (조합)
# from itertools import permutations (순열)
# list(combinations(list, number))

answer = 0

def solution(numbers):
    global answer
    cards = []
    # 숫자 조합 카드들 담는 리스트
    for cnt in range(1, len(numbers)+1):
    # 1자리수부터 numbers의 모든 숫자 조합한 자리수까지
        tuple_card = permutations(numbers, cnt)
        # 흩어진 종이 조각을 붙여
        # 튜플 반환
        for i in tuple_card:
            final_card = "".join(i)
            # str형 공백없이 join
            cards.append(int(final_card))
            # int 변환
    prime_number(set(cards))
    # 중복 제거
    return answer

def prime_number(lst):
# 소수를 몇 개 만들 수 있는지
    global answer
    for num in lst:
        cnt = 0
        # 1외에 나누어지는 횟수
        for i in range(2, num):
        # 2부터 num-1을 나눈 경우
            if num%i==0:
                cnt += 1
                break
                # 1번이라도 나누어지면 for문 종료
                # 시간초과 방지
        if num > 1 and cnt==0:
        # 숫자가 1보다 큰 경우
        # 숫자가 1이 외의 숫자로 나누어지지 않는 경우
            answer+=1
            # 소수의 개수 정답 추가