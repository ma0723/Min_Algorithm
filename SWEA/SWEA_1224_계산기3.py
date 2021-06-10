import sys
sys.stdin = open("1224.txt", "r")

def is_number(x):
# 피연산자 판별
    if x not in operator and x not in braket:
        return True
    else:
        return False

def isp(token):
# stack top 우선순위
    if token == "*":
        return 2
    elif token == "+":
        return 1
    elif token == "(":
        return 0
        # top에 이미 존재하는 열린 괄호는 가장 우선순위가 낮다

def icp(token):
# stack push 우선순위
    if token == "*":
        return 2
    elif token == "+":
        return 1
    elif token == "(":
        return 3
        # push하는 열린 괄호는 가장 우선순위가 높다

T = 10
for tc in range(1, T+1):
    N = int(input())
    # 테스트 케이스의 길이
    infix = list(input())
    # 중위표기법 list

    postfix = []
    # 후위표기법 list
    stack = []
    operator =["*","+"]
    # 연산자
    # 문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 피연산자인 숫자는 0 ~ 9의 정수
    braket = ["(",")"]
    # 괄호

    for i in infix:
        if is_number(i):
        # 피연산자 (True)
            postfix.append(i)
            # 후위표기법 출력물 추가
        elif i == ")":
        # 닫힌 괄호
            while stack:
            # stack에 자료가 존재하는 동안
                top = stack.pop()
                # stack top pop
                if top == "(":
                # stack top pop을 한 경우 열린 괄호일 때
                    break
                    # while문 종료
                postfix.append(top)
                # stack top pop을 한 경우 열린 괄호가 아닐 때(피연산자 혹은 연산자)
                # 후위표기법 출력물 추가
        else:
        # 열린 괄호 혹은 연산자
            if len(stack) == 0:
            # stack이 비어있으면
                stack.append(i)
                # stack push
            else:
            # stack의 자료가 존재하는 경우
            # 우선순위 비교
                while stack:
                # stack에 자료가 존재하는 동안
                    top = stack[-1]
                    if icp(i) > isp(top):
                    # icp() stack push 우선순위
                    # isp() stack top 우선순위
                        stack.append(i)
                        # stack push
                        break
                        # while문 종료
                    postfix.append(stack.pop())
                    # 후위표기법 출력물 추가
                    if len(stack) == 0:
                    # 스택이 비어있는 경우
                    # 유의
                        stack.append(i)
                        # stack push
                        break
                        # while문 종료
    while stack:
        postfix.append(stack.pop())

    stack2 = []
    for i in postfix:
    # 후위표기법 순회
        if len(stack2) == 0:
        # 비어있는 경우
            stack2.append(int(i))
            # stack push
        else:
            if is_number(i):
            # 피연산자(True)
                stack2.append(int(i))
                # stack push
                # str을 정수형 전환 int()
            else:
            # 연산자
                num1 = stack2.pop()
                num2 = stack2.pop()
                # stack의 피연산자를 2번 pop
                if i == "+":
                    num = num1 + num2
                else:
                    num = num1 * num2
                stack2.append(num)
                # stack push

    print("#{} {}".format(tc, stack2[0]))
    # 최종적으로 stack에는 하나의 값만 남는다




