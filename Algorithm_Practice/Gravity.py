'''
3 # 3개 입력 3개 반복
9 # 가로 길이
7 4 2 0 0 6 0 7 0 # 상자 높이(세로로 몇 개 쌓는가)
9
7 4 2 0 0 6 7 7 0
20
52 56 38 77 43 31 11 87 68 64 88 76 56 59 46 57 75 85 65 53
'''

# test case 반복
# 입력 / 계산 / 출력
# 2차원 배열

# test case 반복
T = int(input())
# input 한줄 읽기
# int 정수형 형변환
for tc in range(1, T+1):
# test case 반복하는 for문

    #1 입력
    N = int(input())
    boxTop = list(map(int, input().split()))
    # 공백을 기준으로 분할(.split())
    # 정수형 변환(map(int, ))
    # 한 줄 읽기(input())
    room = [[0 for _ in range(100)] for _ in range(N)]
    # 상자 높이 [0 for _ in range(100)] 100번을 0을 찍어라 '_'는 i 대신 의미 없다는 표시
    # 가로 길이 for _ in range(N)
    # for row in room:
    # print(row)
    for i in range(N):
    # 가로 행
        for j in range(boxTop[i]):
        # 세로 열 높이
            room[i][j] = 1
            # 가로 길이 0부터 N-1까지 상자 높이 0의 100칸 높이 중에 boxTop에 적혀진 각자 높이(7)만큼 1을 7번 채워라
            # (0,0) (0,1) (0,2)...(0,6)까지 7번 채우는 이중 for문 index
            # room[i][j] index
            # boxTop[i]는 세로 상자의 높이를 담은 리스트

    #2 계산
    my_max = 0
    # 최대 낙차 초기값 저장
    for i in range(N):
    # 각 행마다
        if boxTop[i] > 0:
        # 1이 채워져 있는 경우(상자 높이가 존재하는 경우)
            dist = 0
            # 개수 초기값
            for j in range(i+1, N):
            # 1이 있는 다음칸부터 세어간다
            # 상자가 존재하는 경우 낙차하는 개수를 세기 때문에 현재 위치 제외
                if room[j][boxTop[i]-1]==0:
                # 행 고정 열 변화
                # index는 상자 높이-1 (boxTop[i]-1)
                # 높이는 1부터 시작하므로 1을 뺴야 0부터 시작하는 인덱스와 일치
                # 0으로 인덱스의 값이 비어있는 경우 (낙차 높이)
                    dist += 1
                    # 0의 개수(낙차 높이)를 센다
            if my_max < dist:
                my_max = dist
                # 초기값 0과 비교하여 최대 낙차 높이 
    #3 출력
    print(f'#{tc} {my_max}')
    # f-string
    print("#{} {}".format(tc, my_max))
    # str.format