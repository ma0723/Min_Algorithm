import heapq
# 최소힙이 기본값
# 최대힙을 원하면 튜플이나 리스트의 순서 idx를 가장 앞에 넣고 -를 붙인다

data = [[1, "a"], [2, "b"], [3, "c"]]

new_data = []

for i in data:
    new_data.append([-i[0], i[1]])

heap = []

for i in new_data:
    heapq.heappush(heap, i)

first = heapq.heappop(heap)
second = heapq.heappop(heap)
print(first[1])
print(second[1])
#최대힙 구현을 위해 인덱스에 -를 붙이기