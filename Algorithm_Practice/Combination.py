import itertools

# 순열 (순서가 있는 경우)
perm_result = list(itertools.permutations(['1', '2', '3'], 2))
print("경우의 수 {}개".format(len(perm_result)))
print(perm_result)

# 조합 (순서가 없는 경우)
comb_result = list(itertools.combinations(['1', '2', '3'], 2))
print("경우의 수 {}개".format(len(comb_result)))
print(comb_result)

from itertools import permutations, combinations, product, combinations_with_replacement

data = ['A', 'B', 'C'] # 데이터 준비
result = list(permutations(data, 3)) # 모든 순열 구하기
print(result)

result = list(combinations(data, 2)) #2개를 뽑는 모든 조합 구하기
print(result)

result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기(중복 허용)
print(result)

result = list(combinations_with_replacement(data, repeat=2)) # 2개를 뽑는 모든 조합 구하기(중복 허용)
print(result)

# #3개를 뽑는 순열
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
# #2개를 뽑는 조합
# [('A', 'B'), ('A', 'C'), ('B', 'C')]
# #2개를 뽑는 중복허용 순열
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
# #2개를 뽑는 중복허용 조합
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]