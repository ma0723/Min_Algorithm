# 가로, 세로를 모두 보아 가장 긴 회문의 길이
# 각 칸의 들어가는 글자는 'A', 'B', 'C' 중 하나
# ABA도 회문이며, ABBA도 회문이다. A또한 길이 1짜리 회문

import sys
sys.stdin = open("1216.txt", "r")

def find(t):
    result = []
    # 빈 리스트 초기값 설정
    for i in range(1, 100):
    # 회문의 길이 1부터 100까지
        for j in range(100-i+1):
        # i개의 글자가 회문인지 판별
        # 시작점을 0부터 N-i까지 인덱스
            cnt = 0
            # 앞뒤글자 일치하는 개수 초기값
            if i == 1:
            # i가 2 이상인 경우 몫이 1이 나오기 때문에 1인 경우와 분리
                result.append(i)
                # 회문의 길이 1 result(list)에 추가
            else:
            # i가 2 이상인 경우 몫이 1이 나오기 때문에 1인 경우와 분리
                for k in range(i//2):
                    if t[j+k] == t[j+i-1-k]:
                    # 시작 인덱스+ k와 마지막 인덱스 + k의 값이 같다면
                    # 첫번째 글자와 뒤에서 첫번째 글자
                    # 두번째 글자와 뒤에서 두번째 글자
                        cnt += 1
                    else:
                        break
                        # k의 for문 종료
                if cnt == i//2:
                    result.append(i)
                    # 회문의 길이 result(list)에 추가
                else:
                    pass
    ans = 0
    for i in result:
        if ans < i:
            ans = i
    return ans
    # 가로 읽기, 세로 읽기 1줄당 회문 길이 최대값

T = 10
for tc in range(1, T+1):
    N = int(input())
    lst = [[i for i in input()] for _ in range(100)]
    # 100x100 2차원 배열

    result1 = []
    # 가로 읽기 N줄 담을 list
    result2 = []
    # 세로 읽기 N줄 담을 list

    for i in range(100):
    # 행 우선 탐색
    # 가로 읽기
        str1 = ''
        # 가로 읽기 1줄당 담을 str
        for j in range(100):
            str1 += lst[i][j]
        result1.append(str1)

    for i in range(100):
    # 열 우선 탐색
    # 세로 읽기
        str2 = ''
        # 세로 읽기 1줄당 담을 str
        for j in range(100):
            str2 += lst[j][i]
        result2.append(str2)

    my_max = []
    for i in range(100):
    # 가로 읽기 100개
    # 세로 읽기 100개
        ans1 = find(result1[i])
        ans2 = find(result2[i])
        # 가로 읽기, 세로 읽기 1줄당 회문 길이 최대값
        my_max.append(ans1)
        my_max.append(ans2)

    final_max = 0
    for i in my_max:
        if final_max < i:
            final_max = i
    print("#{}".format(tc), end = " ")
    print(final_max)
