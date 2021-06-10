import sys
sys.stdin = open("1231.txt", "r")

T = 10
# 총 10개의 테스트 케이스가 주어진다
for tc in range(1, T+1):
    N = int(input())
    # 트리가 갖는 정점의 총 수 N(1≤N≤100)이 주어진다
    num_list = [list(input().split()) for _ in range(N)]
    # N줄에 걸쳐 각각의 정점 정보 (정점번호는 1부터 N까지의 정수로 구분)
    # 루트 정점의 번호는 반드시 1

    tree = [[0] * 3 for _ in range(N + 1)]
    # 트리는 완전 이진 트리 형식

    for i in range(N):
    # num_list 순회하는 for문
        for j in range(len(num_list[i])):
        # 각 정점 번호 순회하는 for문
            number = int(num_list[i][0])
            # 부모 인덱스
            string = num_list[i][1]
            # 출력 문자열
            if j==2:
                tree[number][0] = int(num_list[i][j])
                # 왼쪽 자식 노드 저장
            if j==3:
                tree[number][2] = int(num_list[i][j])
                # 오른쪽 자식 노드 저장
            tree[number][1] = string

    print("#{}".format(tc),end=" ")
    def inorder(node_index):
    # 중위 순회
        if node_index:
        # 유효하면(0이 아니라면)
            inorder(tree[node_index][0])
            print('{}'.format(tree[node_index][1]), end="")
            # 순서 경로에 따른 문자열 출력
            inorder(tree[node_index][2])

    inorder(1)
    print()

for tc in tnage(1, 11):
    N = int(input())
    tree = [[0, 0, 0]]
    # 초기화 인덱스 0 채우기
    for _ in range(N):
        n_input = input().split()
        node = [0, 0, 0]
        # node를 기본적으로 0을 채워야 자식 노드가 없어도 인덱스 에러 방지
        for idx, value in enumerate(n_input):
            if idx == 1:
                node[0] = value
                # 문자열
            elif idx == 2 or idx= = 3:
                node[idx-1] = int(value)
                # 자식노드 정수형 전환 후 저장

    result = ''

    def inorder(node_index):
    # 중위 순회
        if node_index:
        # 유효하면(0이 아니라면)
            inorder(tree[node_index][1])
            result += tree[node_index][0]
            inorder(tree[node_index][2])

    inorder(1)

    print('#{} {}'.format(tc, result))