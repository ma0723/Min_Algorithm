import sys
sys.stdin = open("7465.txt","r")

def find_set(x):
# 대표 부모 노드 찾아가는 함수
    while p[x] != x:
        x = p[x]
    return x
def union(x, y):
# 합집합
    p[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 각각 창용 마을에 사는 사람의 수 N
    # 서로를 알고 있는 사람의 관계 수 M

    p = [i for i in range(N + 1)]
    # 창용 마을에는 N명의 사람이 살고 있다 1번부터 N번까지
    # 자기 자신을 대표로 가지는 부모 배열 

    edge = []
    # 간선 정보 리스트
    for _ in range(M):
    # M개의 줄에 걸쳐서 서로를 알고 있는 두 사람의 번호
        u, v = map(int, input().split())
        union(u, v)
        # 두 사람이 서로 아는 관계이거나 몇 사람을 거쳐서 알 수 있는 관계라면 무리
        # 자기자신을 대표자로 가지지 않고 연결된 정점 사람으로 대표자 할당

    result = 0
    # 무리의 수
    for n in range(1, N + 1):
    # 1번부터 N번까지
        if p[n] == n:
        # 자신이 대표이면
        # 대표의 수 = 무리의 수
        # 그 외의 같은 무리들은 대표를 향해 p[idx]의 값 할당
            result += 1

    print('#{} {}'.format(tc, result))
