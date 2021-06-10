import sys
sys.stdin = open("2005.txt", "r")

def tri(N):
    lst = [[0]*N for _ in range(N)]
    # 2차원 배열 리스트 초기값 NXN
    for i in range(N):
    # 크기 N인 파스칼의 삼각형
    # 행 N개 (인덱스 0~N-1)
        for j in range(N):
        # 열 1~N개 (인덱스 0~N-1)
        # 행 고정 열 변화
            if i==0 and j==0:
                lst[i][j] = 1
                # 첫 번째 줄은 항상 숫자 1
                break
                # j for문 종료(1행 1열만 1로 삽입 후 다음 행)
                # i for문 순회(2행)
            else:
            # 두 번째 줄부터 각 숫자들은 자신의 왼쪽(-1행-1열)과 오른쪽 위(-1행)의 숫자의 합
                if j==0:
                # 왼쪽 위가 없는 경우(각 행의 1열)
                    lst[i][j] = lst[i-1][j]
                    # 오른쪽 위(-1행)의 숫자
                    # 1
                elif i==j:
                # 오른쪽 위가 없는 경우(각 n행의 n열)
                    lst[i][j] = lst[i-1][j-1]
                    # 왼쪽(-1행-1열)의 숫자
                    # 1
                else :
                # 둘다 존재하는 경우
                    lst[i][j] = lst[i-1][j-1] + lst[i-1][j]
                    # 왼쪽(-1행-1열)과 오른쪽 위(-1행)의 숫자의 합
    return lst

T = int(input())
for tc in range(1, T+1):
    print("#{}".format(tc))

    N = int(input())
    result = tri(N)
    # N을 입력 받아 크기 N인 파스칼의 삼각형

    for i in result:
    # 2차원 배열 
    # 행 고정 열 변화
    # 행 우선 탐색
        for j in i:
            if j!=0:
                print(j, end = ' ')
                # 리스트의 각 0이 아닌 요소를 공백 한 칸을 기준으로 가로 출력
            else:
                pass
                break
                # 0으로 비어있는 경우 진행중인 행의 출력 j for문 종료
        print()
        # 다음행의 출력시 개행