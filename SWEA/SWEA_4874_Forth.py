import sys
sys.stdin = open("4874.txt", "r")

T = int(input())
for tc in range(1, T+1):
    str = list(input().split())
    # 피연산자와 연산자는 여백으로 구분
    # 코드는 ‘.’로 끝
    stack = []
    flag = 0
    for i in str[:-1]:
    # ‘.’은 스택에서 숫자를 꺼내 출력
    # 코드는 ‘.’로 끝
        if i != '+' and i != '-' and i != '*' and i != '/':
        # 피연산자 숫자
            stack.append(int(i))
            # stack push
        else:
        # 연산자 혹은 '.'을 만나면
        # 스택의 숫자 두 개 stack pop
            try:
            # 후위표기법 계산
                if i == '+':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    num = num1 + num2
                    stack.append(num)
                    # 결과를 다시 스택에 넣는다 stack push
                elif i == '-':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    num = num2 - num1
                    # 나중에 pop한 숫자에서 먼저 pop한 숫자 빼기
                    stack.append(num)
                    # 결과를 다시 스택에 넣는다 stack push
                elif i == '*':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    num = num1 * num2
                    stack.append(num)
                    # 결과를 다시 스택에 넣는다 stack push
                elif i == '/':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    num = num2 / num1
                    # 나중에 pop한 숫자에서 먼저 pop한 숫자 나누기
                    # 나눗셈의 경우 항상 나누어 떨어진다
                    stack.append(num)
                    # 결과를 다시 스택에 넣는다 stack push
            except:
            # 오류발생
                flag=99999

    if len(stack) == 1 and flag == 0:
    # stack의 길이가 1인 경우
        print("#{} {}".format(tc, int(stack[0])))
        # 계산결과를 정수로 출력
    elif len(stack) > 1 or flag==99999:
    # stack의 길이가 1이 아닌 경우
        print("#{} {}".format(tc, 'error'))
        # 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력

def find():
    s = []
    for i in range(len(code)):
        if code[i] =='+' or code[i] == '-' or code[i] == '/' or code[i] == '*':
        # 연산 작업
            if len(s) >= 2:
            # 스택의 길이가 2이상
                op2 = int(s.pop())
                # 피연산자 stack pop
                op1 = int(s.pop())
                # 피연산자 stack pop
                if code[i] == '+':
                    s.append(op1+op2)
                elif code[i] == '-':
                    s.append(op1-op2)
                elif code[i] == '*':
                    s.append(op1*op2)
                elif code[i] == '/':
                    s.append(op1//op2)
                    # 각 연산에 맞춰서 연산을 하고 결과를 다시 stack push
                    # 정수형 출력을 위해 //

            else:   
            # 연산하려고 하는데 스택에 2개 미만
                return 'error'
                # error 출력
        elif code[i] != '.' : 
        # 마침표가 아니면 (숫자면)스택에 넣음
            s.append(code[i])
        elif code[i] == '.' :  
        # 출력
            if len(s) == 1: 
            # 스택에서 숫자가 1
                return s.pop()
            else:
            # 스택에서 숫자가 1개가 남은 경우가 아닌 경우
                return 'error'
                # error 출력

T = int(input())
for tc in range(1,T+1):
    code = list(input().split())
    # print(code)
    print("#{} {}".format(tc, find()))
