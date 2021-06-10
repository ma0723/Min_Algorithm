import sys
sys.stdin = open("5178.txt", "r")

def post_order(node_idx):
# 후위순회
    if node_idx <= N:
    # 유효한 경우
        left = post_order(node_idx*2 )
        right = post_order(node_idx*2 + 1)
        tree[node_idx] = tree[node_idx] + left + right
        return tree[node_idx]
    return 0
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    # 노드의 개수 N과 리프 노드의 개수 M, 값을 출력할 노드 번호 L
    tree = [0] * (N + 1)
    # 완전 이진 트리
    for _ in range(M):
        index, value = map(int, input().split())
        tree[index] = value
    post_order(1)
    print("#{} {}".format(tc, tree[L]))

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    # 노드의 개수 N과 리프 노드의 개수 M, 값을 출력할 노드 번호 L
    leaf = [list(map(int, input().split())) for _ in range(M)]
    tree = [0] * (N + 1)
    # 완전 이진 트리
    # M개의 줄에 걸쳐 리프 노드 번호(idx)와 1000이하의 자연수(value)
    # N개의 노드를 갖는 완전 이진 트리의 노드 번호는 루트가 1번이 되며, 같은 단계에서는 왼쪽에서 오른쪽으로 증가, 단계가 꽉 차면 다음단계의 왼쪽부터 시작

    # height = 0
    # while N//2:
    #     N = N//2
    #     height += 1

    for i in range(M):
    # leaf 노드 순회하는 for문
        tree[leaf[i][0]] = leaf[i][1]
        # leaf node idx leaf node value 할당

    for i in range(len(tree)-1, 1, -1):
    # leaf 노드에서 역순 순회하는 for문
    # 후위순회(자식 좌우 -> 부모)
        if tree[i] == 0:
            if 2*i+1 <= N:
            # 완전 이진트리이기 때문에 우측 자식 노드가 있는 경우
                tree[i] = tree[2*i] + tree[2*i+1]
            else:
            # 좌측 자식노드만 있는 경우
                tree[i] = tree[2 * i]

    print("#{} {}".format(tc, tree[L]))


