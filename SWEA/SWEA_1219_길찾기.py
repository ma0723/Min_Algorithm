import sys
sys.stdin = open("1219.txt", "r")

def dfs(n, lst):
    lst.append(n)
    if adj1[1][n] != -1:
    # 연결 (adj1[1][n] =! -1)
    # 방문하지 않은 경우의 조건 불요 거슬러 올라갈 수 없다
    # 2가지 갈림길로 가는 모든 경우의 수를 담아야 해서 연결되어 있는 여부만 본다
            dfs(adj1[1][n], lst)
            if adj2[1][n] != -1:
            # 2번째 갈림길도 존재하는 경우
                dfs(adj2[1][n], lst)
                # 인접한 위치 i로 이동
                # 같은 행동 반복
T = 10
for tc in range(1, T+1):
    num, E = map(int, input().split())
    # 첫 줄에는 테스트 케이스의 번호와 길의 총 개수

    edge = list(map(int, input().split()))
    # 그 다음 줄에는 나열된 순서대로 순서쌍

    V = len(set(edge))
    # 정점의 개수
    # A와 B는 숫자 0과 99
    # 정점(분기점)의 개수는 98개(출발점과 도착점 제외)를 넘어가지 않으며 (개수가 최대 100)


    adj1 = [[i for i in range(100)], [-1 for _ in range(100)]]
    adj2 = [[i for i in range(100)], [-1 for _ in range(100)]]
    # 인접행렬 대신 size [100]의 정적 배열 2개을 선언하여, 각 정점의 번호를 주소
    # 한 개의 정점에서 선택할 수 있는 길의 개수도 2개를 넘어가지 않는다(최대 2개의 갈림길)
    # 모든 길은 일방 통행으로 되돌아오는 것이 불가능(방향 그래프)

    for i in range(E):
        for j in range(100):
            if edge[i*2] == j:
            # 시작점
                if adj1[1][j] == -1:
                # 첫번째 간선의 도착지가 입력되지 않은 경우
                    adj1[1][j] = edge[i * 2 + 1]
                    # adj1 2행 j열(시작점의 값)
                    # 도착점
                else:
                # 첫번째 간선의 도착지가 입력된 경우
                    adj2[1][j] = edge[i*2+1]
                    # adj2 2행 j열(시작점의 값)
                    # 도착점
    lst = []
    dfs(0, lst)

    if 99 in lst:
        print("#{} {}".format(tc, 1))
    else:
        print("#{} {}".format(tc, 0))
    # A도시(0)에서 출발하여 B도시(99)로 가는 길이 존재하면 1 아니면 0