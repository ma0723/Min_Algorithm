arr = [-7,-3,-2,5,8]

n = len(arr)
# 원소의 개수

my_big_list = []
for i in range(1<<n):
# 부분집합의 개수
    my_small_list = []
    for j in range(n):
    # 원소의 개수만큼 비트를 교환
        if i&(1<<j):
        # i의 j번째 비트가 1이면 j번째 원소를 출력
            my_small_list.append(arr[j])
    my_big_list.append(my_small_list)
print(my_big_list)
print(len(my_big_list))

for i in my_big_list:
    my_sum = 0
    for j in i:
        my_sum += j
    if my_sum == 0:
        print('True')
    else:
        print('False')
