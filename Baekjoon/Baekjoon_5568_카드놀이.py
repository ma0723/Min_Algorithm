from itertools import permutations


n. k = map(int, input().split())
# 상근이는 카드 n(4 ≤ n ≤ 10)장을 바닥
# 상근이는 이 카드 중에서 k(2 ≤ k ≤ 4)장을 선택하고, 가로로 나란히

cards = [input().split() for _ in range(n)]
# 셋째 줄부터 n개 줄에는 카드에 적혀있는 수
# 조합 혹은 순열을 위해서는 str형태로 숫자를 입력
result = set()
# 숫자 중복 제거
for per in permutations(cards, k):
# 상근이가 만들 수 있는 정수는 모두 몇 가지
# 숫자 문자열 순열, 조합
    result.add(''.join(per))
    # 순열의 모든 값을 공백없이 str을 합친다
    # set()에 요소를 추가할 때에는 add()

