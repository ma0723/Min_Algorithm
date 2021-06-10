import sys
sys.stdin = open("5248.txt","r")

def DFS(idx):
    global team
    if idx in result:
    # 이미 정점이 팀원추가한 전체 팀원의 수에 존재하는 경우
        return
    else:
        if not visited[idx]:
        # 방문하지 않은 경우
            team.add(idx)
            # 팀원추가
        visited[idx] = 1
        # 방문표시
        for i in range(1, N+1):
            if adj[idx][i] == 1 and not visited[i]:
            # 인접 연결
            # 방문하지 않은 경우
                visited[i] = 1
                # 방문표시
                team.add(i)
                # 팀원추가
                DFS(i)
                # 완전탐색 / 재귀
    
T = int(input())
for tc in range(1, T+1):
    # 같은 조에 참여하고 싶은 사람끼리 두 사람의 출석 번호를 종이에 적어 제출

    # 한 사람이 여러 장의 종이를 제출하거나 여러 사람이 한 사람을 지목한 경우 모두 같은 조
    # 1-2 2-3 -> 1-2-3
    # 번호를 적지도 않고 다른 사람에게 지목되지도 않은 사람은 단독으로 조
    # 4

    N, M = map(int, input().split())
    # 첫 줄에 N과 M
    # 1번부터 N번까지의 출석번호가 있고, M 장의 신청서가 제출
    MList = list(map(int, input().split()))

    adj = [[0]*(N+1) for _ in range(N+1)]
    # 인접행렬
    visited = [0]*(N+1)
    # 방문배열

    for i in range(M):
    # 다음 줄에 M 쌍의 번호
        adj[MList[2*i]][MList[2*i+1]] = 1
        adj[MList[2*i+1]][MList[2*i]] = 1
        # 무방향 그래프

    result = []
    # 팀원추가한 전체 팀원
    for i in range(1, N+1):
        team = set([])
        # 각 팀
        DFS(i)
        # 완전탐색
        if team:
        # 팀이 존재하는 경우
            result.append(team)
            # 1번부터 N번까지의 출석번호가 있고, M 장의 신청서가 제출되었을 때 전체 몇 개의 조

    print("#{} {}".format(tc, len(result)))

def find_set(x):
# 대표원소 찾아서 모두 바꾸기
    while p[x] != x:
    # 대표원소 찾을 떄까지
        x = p[x]
    return x
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    p = [i for i in range(N+1)]
    # 대표원소 초기화 (자기자신이 대표원소)
    for i in range(M):
    # Union
        a, b = arr[i*2], arr[i*2+1]
        p[find_set(b)] = find_set(a)
        # b의 대표원소 찾아서 a의 대표원소로 바꾸기 (Union)
        # 2, 3의 경우 3의 대표원소 3을 2로 바꾸기
    cnt = 0
    for i in range(1, N+1):
    # 대표원소수 = 그룹수
        if p[i] == i:
        # 다른 숫자가 대표원소가 아니라 자기 자신이 대표원소인 경우
            cnt += 1
    print("#{} {}".format(tc, cnt))