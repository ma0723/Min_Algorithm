def isEmpty():
# 공백 상태 여부
    return r == f

def isFull():
# 포화 상태 여부
    return r == len(q)-1

def enQueue(data):
# 큐에 데이터 삽입
    global r
    # 값을 변경해서 global 필요
    if isFull():
        print("Queue Full")
    # 포화상태인 경우
    else:
    # 포화상태가 아닌 경우
        r += 1
        q[r] = data
        # 삽입(enQueue)

def deQueue():
# 큐에 데이터 제거
    global f
    # 값을 변경해서 global 필요
    if isEmpty():
    # 비어있는 경우
        print("Queue Empty")
    else:
    # 원소가 있는 경우
        f += 1
        return q[f]
        # 삭제(deQueue)

# 배열
n = 5
q = [0]*n
f = r = -1

# 큐에 자료 삽입하기
enQueue(1)
enQueue(2)
enQueue(3)
print(q)
enQueue(4)
enQueue(5)
print(q)
enQueue(6)
print(q)
# 큐에서 자료 꺼내기
d1 = deQueue()
print(d1)
print(q)    #큐에서 자료를 삭제하지는 않음
print('front : ', f)    #첫번째원소 가르키는 front의 위치 변경
d2 = deQueue()
print(q, d2)
print('front : ', f)    #첫번째원소 가르키는 front의 위치 변경

'''
선형큐의 문제점 -> 자료를 수정하면서 알아보기
'''
