import sys
sys.stdin = open("5186.txt", "r")

# 0보다 크고 1미만인 십진수 N을 이진수
# 소수점 아래가 12자리 이내인 N이 주어진다

def Binary(num):
    global result
    for i in range(1, 13):
        num *= 2
        # 2를 곱해야 가장 앞자리 소수점이 1의 자리 몫으로 넘어온다
        result += str(int(num) % 2)
        # N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자를 출력
        # 나머지는 1 혹은 0 str
        # 몫
        if num%1 == 0.0:
            return
    else:
        result = 'overflow'
        return

T = int(input())
for tc in range(1, T + 1):
    number = float(input())
    # 부동소수점 입력
    result = ''
    # 0.을 제외한 나머지 숫자를 출력
    Binary(number)

    print('#{} {}'.format(tc, result))