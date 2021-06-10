import sys
sys.stdin = open("5185.txt", "r")



hex_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

T = int(input())
for tc in range(1, T+1):
    print("#{}".format(tc), end= ' ')
    N, hex = input().split()
    # N 자리수 16진수

    dec = []
    # 10진수 변환 (hex_lst의 index)
    for i in hex:
        for j in range(16):
            if hex_lst[j] == i:
                dec.append(j)
    # print(dec)

    # 2진수 변환
    for i in dec:
        ans = ''
        while i > 0:
            ans = str(i % 2) + ans
            # 나머지 (역순이므로 ans 뒤에 배치)
            i //= 2
            # 몫
            # N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램
            # 2진수의 앞자리 0도 반드시 출력
        if len(ans) != 4:
            my_ans = '0'*(4-len(ans)) + ans
            # 4자리가 모두 채워지지 않은 경우 앞부분 0 채우기
        else:
            my_ans = ans
            # 4자리 모두 채워진 경우
        print(my_ans, end='')
        # 4자리 2진수 공백없이 나열
    print() 
    # 다음문제 개행
