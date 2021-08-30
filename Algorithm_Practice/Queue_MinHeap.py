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

# import heapq

# def heapsort(iterable):
# 	h = []
#     result = []
#     # 모든 원소를 차례대로 힙에 삽입 (부호 반대로)
#     for value in iterable:
#     	heapq.heappush(h, -value)
#     # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기 (부호 다시 뒤집어서)
#     for i in range(len(h)):
#     	result.append(heapq.heappop(h))
#     return result

# result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
# print(result)