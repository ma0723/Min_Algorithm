# union기능
def union(a,b) :
    if find(a) != find(b):
        parent[find(b)] = a
# find 기능
def find(x) :
    # while parent[x] != x:
    #     x = parent[x]
    # return x
    if parent[x] == x:
    # 루트노드라면 해당 노드를 반환
        return x
    else:
        # parents[x]=find(parents[x])
        return find(parent[x])
        # 루트노드가 아니면 부모노드로 이동

n, m = map(int, input().split())
# m은 입력으로 주어지는 연산의 개수

parent = [i for i in range(n+1)]
# 초기에 {0}, {1}, {2}, ... {n} 이 각각 n+1개의 집합

for _ in range(m):
    command, a, b = map(int, input().split())
    if command:
    # 1 a b의 형태
    # 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산
    # 1로 시작하는 입력에 대해서 한 줄에 하나씩 YES/NO로
        if find(a) != find(b):
            print('NO')
        else:
            print('YES')
    else:
    # 0 a b의 형태로 입력
    # a가 포함되어 있는 집합과, b가 포함되어 있는 집합을 합친다
        union(a, b)



