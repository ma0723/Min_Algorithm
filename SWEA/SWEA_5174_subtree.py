import sys
sys.stdin = open("5174.txt", "r")

T = int(input())
for tc  in range(1, T+1):
    E, N = map(int, input().split())
    # 간선의 개수 E와 N
    node = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(E + 2)]
    # E개의 부모 자식 노드 번호 쌍
    # 노드 번호는 1번부터 E+1번까지 존재 range(E + 2)

    parent = 0
    for idx, number in enumerate(node):
    # 부모 노드 인덱스 / 자식 노드 값
        if idx%2:
        # 자식 노드(홀수)
            child = number
            if not tree[parent][0]:
            # 왼쪽 자식 노드가 없는 경우
                tree[parent][0] = child
                # 왼쪽 자식 노드 저장
            else:
            # 왼쪽 자식 노드가 있는 경우 
                tree[parent][2] = child
                # 오른쪽 자식 노드 저장
        else:
        # 부모 노드(짝수)
            parent = number
            # 부모 인덱스 저장

    lst = []
    def preorder(node_index):
    # 전위 순회
        if node_index:
        # 유효하면(0이 아니라면)
            lst.append(preorder(tree[node_index][1]))
            # 서브 트리 노드의 개수
            preorder(tree[node_index][0])
            preorder(tree[node_index][2])

    preorder(N)
    cnt = len(lst)
    # 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내는 프로그램
    # 부모가 없는 노드가 전체의 루트 노드
    # cnt 변형하려면 def global cnt 입력

    print("#{} {}".format(tc, cnt))


def preorder(node_index):
# 전위순회
    global result
    # 재귀함수이기 때문에 값 변경을 위한 global
    if node_index:
    # 유효하면(0이 아니라면)
        result += 1
        # 서브 트리 노드의 개수
        preorder(tree[node_index][0])
        preorder(tree[node_index][2])


T = int(input())
for tc  in range(1, T+1):
    E, N = map(int, input().split())
    # 간선의 개수 E와 N
    data = list(map(int, input().split()))

    tree = [[0]*3]

    i = 0
    while i < E*2:
        parent = data[i]
        child = data[i+1]
        i += 2
        if not tree[parent][0]:
            tree[parent][0] = child
        else:
            tree[parent][2] = child

    result = 0
    preorder(N)

    print("#{} {}".format(tc, result))
