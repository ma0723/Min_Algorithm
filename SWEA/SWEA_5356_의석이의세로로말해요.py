import sys
sys.stdin = open("5356.txt", "r")

# 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’
# 왼쪽에서 오른쪽으로 한 자리씩 이동 하면서 동일한 자리의 글자들을 세로로 읽어 나간다
# 다섯 개의 단어들의 글자 개수는 서로 다를 수 있다
# 세로로 읽은 순서대로 글자들을 공백 없이 출력
T = int(input())
for tc in range(1, T+1):
    lst = [list(input()) for _ in range(5)]
    # 2차원 배열 list
    col = [[-1]*15 for _ in range(5)]
    # 각 줄에는 길이가 1이상 15이하인 문자열
    # 다섯 개의 단어
    # 카운팅 정렬

    len_lst = []
    for i in lst:
        len_lst.append(len(i))

    for i in range(5):
    # 행 5개
        for j in range(len_lst[i]):
        # 행 고정 열 변화
            col[i][j] = lst[i][j]

    str = ''
    for i in range(15):
    # 열 15개
        for j in range(5):
        # 행 5개
        # 열 고정 행 변화
            if col[j][i] == -1:
                pass
            else:
            # -1이 아닌 테스트케이스의 문자가 들어있다면
                str += col[j][i]
                # 세로로 읽기 순서대로 글자에 추가
    print("#{} {}".format(tc, str))

T = int(input())
for tc in range(1, T + 1):

    word = [0]*5
    # 5개의 단어를 담을 리스트
    max_len = 0
    # 최대 길이를 담을 초기값
    for i in range(5):
    # 가로로 읽을 경우
        word[i]  = list(input())
        if len(word[i]) > max_len:
            max_len = len(word[i])


    for i in range(max_len):
    # 세로로 읽을 경우
        for j in range(5):
            #1 오류인 경우 예외처리
            # try:
            #     print(word[j][i], end='')
            # except:
            #     pass
            #2 조건문
            if len(word[j]) > i:
            # 행의 가장 긴 단어의 길이-1까지 진행할 때 그것보다 크다면
            # 행의 가장 긴 단어의 길이와 같거나 클 때
                print(word[j][i], end='')
                # 행 변화 열 고정
                # i=0인 경우 1~5행 중 단어가 1개 이상 있는 해당하는 행만 0열들 출력
                # i=1인 경우 1~5행 중 단어가 2개 이상 있는 해당하는 행만 1열들 출력
                # i=max_len-1인 경우 1~5행 중 단어가 max_len개 있는 해당하는 행만 max_len-1 열들 출력






