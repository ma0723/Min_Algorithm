# ord()
# chr()

def itoa(num):
    remainder = 0
    # 각 자리수를 담을 변수 초기값
    result = ''
    # 문자열을 담을 변수 초기값
    while num:
    # num을 10으로 나눈 몫이 0일 때 종료
    # num != 0
    # num == True
        remainder = num%10
        num //= 10
        result = chr(remainder+ord('0')) + result
        # 나머지부터 구해서 숫자의 가장 뒷자리부터 출력
        # ord('0')를 더해야 아스키코드의 0의 값부터 시작되어 같은 숫자
        # chr() 문자열 변환
    return result

num = int(input())

num_str = itoa(num)

print(num_str, type(num_str))

def itoa(num):
    x = num
    y = 0
    arr = []

    y = x%10
    x = x//10
    arr.append(chr(y+ord('0')))
    print(arr)
