import sys
sys.stdin = open("5202.txt", "r")

def find(idx):
    global result
    # result 값 변경
    if not 0 in visited:
    # 모두 화물차를 방문한 경우
        return
    for i in range(idx, N):
        if result[len(result)-1][1] > time[i][0]:
        # 화물차 작업 시간에 추가한 결과 중 가장 마지막 화물차[-1/len(result)-1]의 종료시간[-1/1]
        # 투입된 화물차 종료시간보다 시작시간이 빠른 경우
        # 제거
            visited[i] = 1
            # 화물차 방문
        if visited[i] == 0 and result[-1][-1] <= time[i][0]:
        # 화물차 방문하지 않은 경우
        # 투입된 화물차 종료시간보다 시작시간이 느린 경우
            visited[i] = 1
            # 화물차 방문
            result.append(time[i])
            # 종료시간이 가장 빠른 인덱스 i 화물차 투입
            find(i+1)
            # 재귀

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 첫 줄에 신청서 N이 주어지고
    time = [list(map(int, input().split())) for _ in range(N)]
    # 다음 줄부터 N개의 줄에 걸쳐
    # 화물차의 작업 시작 시간 s[0]와 종료 시간 e[1]

    # 종료 시간 순서대로
    # 선택 정렬
    for i in range(N):
        for j in range(i+1, N):
            if time[i][1] > time[j][1]:
            # 앞 인덱스가 뒤 인덱스보다 큰 경우
                time[i], time[j] = time[j], time[i]
                # 위치 교환

    result = []
    # 화물차 작업 결과
    # 작업 시작 시간과 완료 시간이 매시 정각을 기준으로 표시
    # 앞 작업의 종료와 동시에 다음 작업을 시작
    visited = [0]*N
    # 방문 배열
    result.append(time[0])
    # 가장 빠른 시작 시간을 가진 화물차 시간 추가
    visited[0] = 1
    # 방문 표시
    find(0)

    print("#{} {}".format(tc, len(result)))
    # 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면
    # 최대 몇 대의 화물차가 이용할 수 있는지(개수)
