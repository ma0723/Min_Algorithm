import sys
sys.stdin = open("5176.txt", "r")


def inorder(node_idx):
# 중위순회
    global cnt
    # 변수 값 변화를 위해 global 선언
    if node_idx < len(tree):
    # 인덱스가 완전 트리의 마지막 인덱스보다 작아야 유효하다
    # 인덱스 에러 방지
        inorder(node_idx * 2)
        tree[node_idx] = cnt
        cnt += 1
        inorder(node_idx * 2 + 1)
        # 왼쪽 서브트리의 루트 < 현재 노드 <오른쪽 서브 트리의 루트인 규칙
        # 중위순회(자식 좌 -> 부모 -> 자식 우)
    # if node_idx > len(tree):
    #     return
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1)
    # 완전 이진 트리 (1차원 배열)
    # 2차원 배열이 아닌 것에 유의

    # height = 0
    # while N//2:
    #     N = N//2
    #     height += 1

    cnt = 1
    inorder(1)

    root = tree[1]
    node = tree[(len(tree)-1)//2]
    # N/2번 노드(N이 홀수인 경우 소수점 버림)에 저장된 값

    print("#{} {} {}".format(tc, root, node))
