'''
f9 : 명령문 위치로 다시 오기 반복문이 있다면 반복하고 오기
f7 : 실행 흐름대로 한줄씩 실행
구문을 누르면 빨간 점 breakpoint 주로 for문
breakpoint 마우스 오른쪽 condition 입력
add to watches : return 값도 같이 보기
'''

# def sum(n):
#     s = 0
#     for i in range(n+1):
#         s = s + i
#     return s
#
#
# result = sum(10)
# print(result)

def sum(n):
    sum = [0] * (n+1)
    for i in range(1,len(sum)):
        sum[i] = sum[i-1] + i
    return sum


num = int(input())
result = [0] * (num+1) # 초기화
result = sum(num)
print(result)