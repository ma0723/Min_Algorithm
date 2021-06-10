# 마이쮸
N = 20

queue = [(1, 0)]
# [0] 첫번째 사람 번호
# [1] 두번째 직전까지 받은 마이쮸 개수
# tuple 초기값

new_people = 1
last_people = 0

while N > 0:
    num, cnt = queue.pop(0)
    # queue [0] FIFO
    last_people = num
    # 마지막으로 받으러 온 사람
    cnt += 1
    # 지난 번보다는 1개 더 가져간다
    
    N -= cnt
    # cnt개수만큼 가져간다
    new_people += 1
    
    queue.append((num, cnt))
    # 맨 뒤로 다시 줄 서기
    queue.append(new_people, 0)
    # 새로운 사람 줄 서기
print(last_people)    
# 20번째 마이쮸를 가져가는 사람
# 2
