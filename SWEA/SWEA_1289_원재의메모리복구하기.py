import sys
sys.stdin = open("1289.txt", "r")

T = int(input())
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
for tc in range(1, T+1):
    origin = input()
    # str로 숫자 한줄 입력
    N = len(origin)
    # 메모리의 길이는 1이상 50이하
    x = '0'
    # str로 입력받아 str 0으로 변수 설정
    cnt = 0
    # 수정 횟수
    for i in range(N):
    # 메모리 bit중 하나를 골라 0인지 1인지 결정하면 해당 값이 메모리의 끝까지 덮어씌우는 것이다.
    # 지금 메모리 값이 0100이고, 3번째 bit를 골라 1로 설정하면 0111
        if origin[i] != x:
            x = origin[i]
            cnt += 1
        # 첫번쨰 자리가 0인 경우 pass
        # 첫번쨰 자리가 1인 경우 우선 1 입력
            # 두번째 자리 == 첫번째 자리 pass
            # 두번째 자리 != 첫번째 자리 다른 값 입력
                # 세번째 자리 == 두번째 자리 pass
                # 세번째 자리 != 두번째 자리 다른 값 입력
    print("#{} {}".format(tc, cnt))
    # 초기화 상태 (모든 bit가 0) 에서 원래 상태로 돌아가는데
    # 최소 수정 횟수를 출력 (모든 경우의 수 cnt 중 최소값)



