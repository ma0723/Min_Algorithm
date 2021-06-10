T = int(input())

for tc in range(T+1):
    N = int(input())
    # 첫째 줄에 트리를 구성하는 노드의 수 N

    parents = [[] for _ in range(N)]

    for _ in range(N-1):
    # 다음 N-1개의 줄에 트리를 구성하는 간선 정보
    # 숫자 A B 가 순서대로 주어지는데, 이는 A가 B의 부모
        parent, child = map(int, input().split())
        parents[child] = parent
        # 부모노드를 담는 방법을 찾기

    # 마지막 줄에 가장 가까운 공통 조상을 구할 두 노드
    a, b = map(int, input().split())

    a_parent = [a]
    b_parent = [b]
    # 각자 자신이 최후 자손노드로서 상위 조상노드 추가

    while parents[a]:
    # 부모들이 계속 존재할 때까지(루트노드는 부모가 없어서 0 종료)
        a_parent.append(parents[a])
        # a의 모든 조상노드 추가
        a = parents[a]

    while parents[b]:
    # 부모들이 계속 존재할 때까지(루트노드는 부모가 없어서 0 종료)
        b_parent.append(parents[b])
        # b의 모든 조상노드 추가
        b = parents[b]

    a_level = len(a_parent) - 1
    b_level = len(b_parent) - 1
    # 같은 공통 조상은 레벨이 같다
    # 인덱스와 조상노드의 개수는 1개씩 차이가 난다

    while a_parent[a_level] == b_level[b_level]:
    # 가장 높은 인덱스부터 1씩 감소
    # 루트노드가 가장 마지막 인덱스
    # 루트노드는 최후의 공통조상
    # 조상노드의 값이 달라지는 순간 while문 종료
    # 바로 직전의 레벨이 가까운 조상 노드드
        a_level -= 1
        b_level -= 1
    print(a_parent[a_level+1])