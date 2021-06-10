import sys
sys.stdin = open("1232.txt", "r")

def post_order(node_idx):
# 후위순회
# 전위순회 전위표기법은 숫자가 뒤쪽 연산자가 앞쪽
    if node_idx:
    # 유효한 인덱스인 경우
        post_order(tree[node_idx][0])
        # 왼쪽 좌식 노드
        post_order(tree[node_idx][2])
        # 오른쪽 자식 노드
        if type(tree[tree[node_idx][0]][1]) != 'str' and type(tree[tree[node_idx][2]][1]) != 'str' and tree[tree[node_idx][0]][1] != 0 and tree[tree[node_idx][2]][1] != 0:
        # 좌우자식 노드의 값이 모두 숫자인 경우(문자가 아닌 경우)
        # ZeroDivisionError 방지하기 위해 [0, 0, 0]으로 이동하는 것 방지(숫자인 경우에도)
        # for i in range(N, 0, -1):
        # 역순으로 순회하면 숫자부터 나온다
            if tree[node_idx][1] == '+':
                tree[node_idx][1] = tree[tree[node_idx][0]][1] + tree[tree[node_idx][2]][1]
            elif tree[node_idx][1] == '-':
                tree[node_idx][1] = tree[tree[node_idx][0]][1] - tree[tree[node_idx][2]][1]
            elif tree[node_idx][1] == '*':
                tree[node_idx][1] = tree[tree[node_idx][0]][1] * tree[tree[node_idx][2]][1]
            else:
                tree[node_idx][1] = tree[tree[node_idx][0]][1] / tree[tree[node_idx][2]][1]

T = 10
for tc in range(1, T+1):
    N = int(input())
    # 트리가 갖는 정점의 총 수 N(1≤N≤1000)
    node = [list(input().split()) for _ in range(N)]
    # N줄에 걸쳐 각각의 정점 정보
    tree = [[0]*3 for _ in range(N+1)]
    # 사칙연산 “+, -, *, /”와 양의 정수로만 구성된 임의의 이진트리

    operators = ['+', '-', '/', '*']

    for i in range(N):
        parent = int(node[i][0])
        # 정점 번호(int)
        if node[i][1] == '+' or node[i][1] == '-' or node[i][1] == '/' or node[i][1] == '*':
        # if node[i][1] in operators:
        # 연산자이면 정점번호, 연산자, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점번호
        # 연산자가 있으면 해당 연산자의 왼쪽 서브 트리의 결과와 오른쪽 서브 트리의 결과를 사용
            tree[parent][0] = int(node[i][2])
            # 왼쪽 자식 노드 저장(int)
            tree[parent][2] = int(node[i][3])
            # 오른쪽 자식 노드 저장(int)
            tree[parent][1] = node[i][1]
            # 연산자 저장
        else:
        # 정점이 단순한 수이면 정점번호와 해당 양의 정수
            tree[parent][1] = int(node[i][1])
            # 양의 정수 저장(int)

    post_order(1)
    result = int(tree[1][1])
    # 중간 과정에서의 연산은 실수 연산으로 하되
    # 최종 결과값이 정수로 떨어지지 않으면 정수부만 출력한다

    print("#{} {}".format(tc, result))
def calculate(left, right, operator):
    if operator == '+':
        return left + right
    elif operator == '-':
        return left - right
    elif operator == '*':
        return left * right
    else:
        return left / right

def post_order(node_idx):
    if node_idx:
        left = post_order(tree[node_idx][0])
        right = post_order(tree[node_idx][2])
        if tree[node_idx][1] in operators:
            return calculate(left, right, tree[node_idx][1])
        else:
            return int(tree[node_idx][1])
    return 0

T = 10
for tc in range(1, T+1):
    N = int(input())
    # 트리가 갖는 정점의 총 수 N(1≤N≤1000)
    tree = [[0]*3 for _ in range(N+1)]

    operators = ['+', '-', '/', '*']

    for _ in range(N):
        data = input().split()
        if data[1] in operators:
            index, operator, left, right = data
            tree[int(index)][0] = int(left)
            tree[int(index)][1] = operator
            tree[int(index)][2] = int(right)
        else:
            index, value = data
            tree[int(index)][1] = value

    result = int(post_order(1))

    print("#{} {}".format(tc, result))