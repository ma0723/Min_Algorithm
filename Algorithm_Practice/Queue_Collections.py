# 큐로 사용할 때: popleft()로 맨 앞 원소 제거, append(x)로 맨 뒤에 원소 x 삽입
# 스택으로 사용할 때: pop()로 맨 뒤 원소 제거, append(x)로 맨 뒤에 원소 x 삽입
# 맨 앞에 원소 x 삽입: appendleft(x)

from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data)) # 리스트 자료형으로 변환

data.popleft()
# 1제거
print(list(data))
data.pop()
# 5제거
print(list(data))