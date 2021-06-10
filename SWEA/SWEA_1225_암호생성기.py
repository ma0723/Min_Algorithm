import sys
sys.stdin = open("1225.txt", "r")

# n개의 수를 처리하면 8자리의 암호
# 8개의 숫자를 입력

# 첫 번째 숫자를 1 감소한 뒤, 맨 뒤
# 다음 첫 번째 수는 2 감소한 뒤 맨 뒤
# 그 다음 첫 번째 수는 3을 감소하고 맨 뒤
# 그 다음 수는 4, 그 다음 수는 5를 감소
# 한 사이클

# 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램은 종료
# 이 때의 8자리의 숫자 값이 암호
# 마지막 암호 배열은 모두 한 자리 수로 구성

for tc in range(1, 11):
    N = int(input())
    # 테스트 케이스의 번호
    arr = list(map(int, input().split()))
    # 8개의 데이터 공백
    cnt = 1
    # 사이클의 감소하는 숫자 초기값
    while True:
        a = arr.pop(0) - cnt
        # front 삭제 
        if a < 0:
        # front 반환한 값이 0보다 작다면
            a = 0
            # 0으로 전환
        arr.append(a)
        # if문에서 0으로 바뀐 경우 rear 삽입
        # if문을 거치지 않더라도 0이상인 경우 그 값을 rear 삽입
        if a == 0:
        # a가 0이 되는 순간
            break
            # while 문 종료
        cnt += 1
        # while문 종료를 거치지 않은 경우 cnt 1씩 증가
        if cnt > 5:
        # cnt가 한 사이클을 순회한 경우
            cnt = 1
            # 초기값 1 복귀
    print('#{}'.format(tc), *arr)


