import sys
sys.stdin = open("4861.txt", "r")

def find(t, N, M):
    for j in range(N-M+1):
    # M개의 글자가 회문인지 판별
    # 시작점을 0부터 N-M까지 인덱스
        cnt = 0
        # 앞뒤글자 일치하는 개수 초기값
        for k in range(M//2):
            if t[j+k] == t[j+M-1-k]:
            # 시작 인덱스+ k와 마지막 인덱스 + k의 값이 같다면
            # 첫번째 글자와 뒤에서 첫번째 글자
            # 두번째 글자와 뒤에서 두번째 글자
                cnt += 1
            else:
                break
                # k의 for문 종료
        if cnt == M//2:
            return j
            # 회문인 경우 시작점 인덱스 반환
        else:
            pass
    return -1
    # 회문이 아닌 경우 -1 반환

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    #  NxN 글자판
    #  길이가 M인 회문을 찾아 출력
    lst = [[i for i in input()] for _ in range(N)]
    # NxN 2차원 배열

    result1 = []
    # 가로 읽기 N줄 담을 list
    result2 = []
    # 세로 읽기 N줄 담을 list

    for i in range(N):
    # 행 우선 탐색
    # 가로 읽기
        str1 = ''
        # 가로 읽기 1줄당 담을 str
        for j in range(N):
            str1 += lst[i][j]
        result1.append(str1)

    for i in range(N):
    # 열 우선 탐색
    # 세로 읽기
        str2 = ''
        # 세로 읽기 1줄당 담을 str
        for j in range(N):
            str2 += lst[j][i]
        result2.append(str2)

    for i in range(N):
    # 가로 읽기 N개
    # 세로 읽기 N개
        ans1 = find(result1[i], N, M)
        ans2 = find(result2[i], N, M)
        if ans1 != -1:
        # 가로 읽기에서 회문인 경우
            print("#{}".format(tc), end = " ")
            print(result1[i][ans1:ans1+M])
            # 반환된 인덱스부터 M개의 글자를 슬라이싱
        elif ans2 != -1:
        # 세로 읽기에서 회문인 경우
            print("#{}".format(tc), end=" ")
            print(result2[i][ans2:ans2+M])
            # 반환된 인덱스부터 M개의 글자를 슬라이싱

