import sys
sys.stdin = open("1961.txt", "r")

def rotate(arr):
# 시계방향 90도 회전 함수
    newArr = [[0]*N for _ in range(N)]
    # 빈 리스트 초기값
    for i in range(N):
        for j in range(N):
        # 행 우선 탐색
            newArr[j][N-1-i] = arr[i][j]
            # 열과 행을 바꾼다
            # [j]
            # 인덱스가 역순(가장 뒤가 가장 앞으로, 가장 앞이 가장 뒤로)
            # [N-1-i]
    return newArr

# N x N 행렬이 주어질 때
# 시계 방향으로 90도, 180도, 270도 회전한 모양
# 입력과는 달리 출력에서는 회전한 모양 사이에만 공백이 존재

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    a = rotate(arr)
    b = rotate(a)
    c = rotate(b)

    print('#{}'.format(tc))
    for i in range(N):
    # 3열 순회, 3,3의 2차원 배열
        print(''.join(map(str,a[i])), ''.join(map(str,b[i])), ''.join(map(str,c[i])))
        # 2차원 배열 안의 리스트(a[i])를 str 타입으로 전환 후(map(str,))
        # 공백없이 붙인다(''.join())
        # 차례로 동시 출력 print(a, b, c)