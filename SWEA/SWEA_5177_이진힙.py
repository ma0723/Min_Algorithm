import sys
sys.stdin = open("5177.txt", "r")

# 항상 완전 이진 트리를 유지하기 위해 마지막 노드 뒤에 새 노드를 추가
# 부모 노드의 값<자식 노드의 값을 유지 (최소힙)
# 새로 추가된 노드의 값이 조건에 맞지 않는 경우, 조건을 만족할 때까지 부모 노드와 값을 바꾼다.
# 마지막 노드의 조상 노드(인덱스//2)에 저장된 정수의 합

def insert(value):
    heap.append(value)
    now_index = len(heap)-1
    while now_index > 0:
        parent_index = now_index//2
        if heap[parent_index] > heap[now_index]:
            heap[parent_index], heap[now_index] = heap[now_index], heap[parent_index]
        now_index = parent_index

def total():
    result = 0
    now_index = len(heap) - 1
    while now_index > 0:
        now_index = now_index//2
        result += heap[now_index]
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_lst = [0] + list(map(int, input().split()))
    # 서로 다른 N개의 자연수가 주어진다

    heap = [0]
    # 1차원 list 이진 트리
    for num in num_lst:
        insert(num)

    print("#{} {}".format(tc, total()))

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_lst = [0] + list(map(int, input().split()))
    # 서로 다른 N개의 자연수가 주어진다
    tree = [0]*(N+1)

    for i in range(1, N+1):
        tree[i] = num_lst[i]
        for j in range(1, i+1):
            while j//2:
                if tree[j//2] > tree[j]:
                    tree[j//2], tree[j] = tree[j], tree[j//2]
                j = j//2

    height = 0
    # 높이 초기값
    number = N
    # N의 값을 유지하기 위해 다른 number로 저장
    while number//2:
    # 몫이 0이 될 때 까지 높이 구하는 while문
        number = number//2
        height += 1
        # 높이 1씩 추가

    result = 0
    # 초기값 설정
    for _ in range(height):
    # 높이 -1 횟수만큼 반복하는 for문
        result += tree[N//2]
        # 조상 노드 정수의 합
        N = N//2
        # 조상 노드를 지속적으로 높이마다 올라가기 위해 N 갱신

    print("#{} {}".format(tc, result))



