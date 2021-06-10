# 2차원 배열
# 순열

# 입력을 파일로 받는 sys
# 가장 상단 파일 상대 경로
import sys
sys.stdin = open("1206.txt", 'r')

# test case 10번 반복하는 for문
# 총 10개의 테스트케이스가 주어진다.
T = 10
for tc in range(1, T+1):

    n = int(input())
    # 첫 번째 줄에는 테스트케이스의 길이
    floor = list(map(int, input().split()))
    # 다음 줄에 테스트 케이스
    # 빌딩의 높이
    # 공백을 기준으로 분할(.split()) ()안에 구별하는 기준 , . 등 삽입 가능
    # 정수형 변환(map(int, ))
    # 한 줄 읽기(input())

    cnt = 0
    # 조망권 개수 초기값 0 설정
    for i in range(2, n - 2):
    # 양쪽 맨 끝 두 칸 제외하고 floor index 추출하는 for문(2부터 n-3까지)
        side_max_floor = 0
        # floor[i]의 양쪽 2개 마다의 최대값을 0으로 초기화
        for j in range(i - 2, i + 3):
            # floor[i]의 양쪽 2개 건물들 floor index 추출하는 for문
            if j != i:
                # floor[i-2] floor[i-1] floor[i+1] floor[i+2] 비교 (j != i)
                if side_max_floor < floor[j]:
                    # 최대값 구하는 if (side_max_floor < floor[j])
                    side_max_floor = floor[j]
                    # 양쪽 2개 건물들 중 높이 최대값을 할당
        if side_max_floor < floor[i]:
            # 양쪽 2개 건물들 중 가장 높이가 높은 건물보다 기준점 건물(floor[i])이 크다면
            cnt += floor[i] - side_max_floor
            # 양쪽 2개의 공백이 존재하는 조망권 개수(차이나는 층수) 초기값 0에 추가

    # 출력
    print(f'#{tc} {cnt}')