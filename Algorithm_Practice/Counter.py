from collections import Counter

counter = Counter(['red', 'blue', 'red' ,'green', 'blue', 'blue'])
print(counter['red']) 
# 2
# 'red'가 등장한 횟수 출력
print(counter['blue']) 
# 3
# # 'blue'가 등장한 횟수 출력
print(dict(counter)) 
# 딕셔너리형으로 변환
# {'red': 2, 'blue': 3, 'green': 1}