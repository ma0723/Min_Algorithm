import sys
sys.stdin = open("input_cal.txt", "r")


def is_number(x):
    if x not in operator and x not in braket:
    # 피연산자인지 확인
        return True
    else:
    # 연산자 혹은 괄호인 경우
        return False


def isp(token):
# isp : 스택의 top 연산자 우선순위
    if token == "*":
        return 2
    elif token == "+":
        return 1
    elif token == "(":
        return 0
        # 가장 바깥 쪽 괄호 우선순위0


def icp(token):
# icp : 스택으로 들어갈 연산자 우선순위
# 들어갈 연산자보다 stack[top]의 연산자가 낮아야 push
# stack[top]이 들어갈 연산자보다 순위가 같거나 높은 경우 pop
    if token == '*':
        return 2
    elif token == '+':
        return 1
    elif token == '(':
        return 3
        # 가장 안쪽 괄호 우선순위3


T = 10
for tc in range(1, T+1):
    N= int(input())
    # tc의 길이    
    infix = list(input())   
    # tc 중위표기법 리스트
    
    postfix = []    
    # 출력결과 저장할 빈 리스트
    stack = []      
    # 스택 빈 리스트
    operator =["*","+"]
    # 연산자
    # 문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 피연산자인 숫자는 0 ~ 9의 정수
    braket = ["(",")"]
    # 괄호

    # 문자열로 된 계산식을 후위 표기식으로 바꾼 후
    # 연산

    for c in infix:
    # 입력된 중위표기법 list 순회하는 for문
        if is_number(c):        
        # 피연산자인 경우(True)
            postfix.append(c)
            # 출력결과 빈 리스트에 값 추가
        elif c ==')':
        # 닫는 괄호
            while len(stack) > 0:
            # 스택에 자료가 있는 동안
                top = stack.pop()
                # pop
                if top =='(':
                # 열린 괄호를 만나면
                    break
                    # pop하지 않고
                    # while문 종료
                postfix.append(top)
                # 출력결과 빈 리스트에 값 추가
        else:
        # 열린 괄호 혹은 연산자
            if len(stack) == 0:
            # 스택이 비어있으면
                stack.append(c)
                # push
            else:
            # 스택이 존재하는 경우 우선순위 비교해서 넣기
                while len(stack) > 0:
                # 스택에 자료가 있는 동안
                    top = stack[-1]
                    # top과 토큰을 비교
                    # stack의 뒤에서 첫번째 인덱스[-1]
                    if icp(c) > isp(top):
                    # icp(c) 들어갈 연산자의 우선순위
                    # isp(top) stack[top]의 우선순위
                        stack.append(c)
                        # 들어갈 연산자의 우선순위가 높으면 push
                        break
                        # while문 종료
                    postfix.append(stack.pop())
                    # 들어갈 연산자의 우선순위가 더 커질 때까지
                    # pop 출력결과 빈 리스트에 값 추가
                    if len(stack) == 0:
                    # 스택이 비어있으면
                        stack.append(c)
                        # push
                        break
                        # while문 종료


    while stack:
    # 스택에 자료가 없어질 때까지
        postfix.append(stack.pop())
        # pop 출력결과 빈 리스트에 값 추가

    stack2 = []
    for c in postfix:
    # 후위표기법 순회
        if len(stack2) == 0:
        # 스택이 비어있으면
            stack2.append(int(c))
            # push
        else:
            if is_number(c):
            # 피연산자인 경우(True)
                stack2.append(int(c))
                # str을 정수형 전환 int()
                # push
            else:
            # 연산자인 경우
                num1 = stack2.pop()
                num2 = stack2.pop()
                # stack의 피연산자를 2번 pop
                if c == '+':
                    num3 = num2 + num1
                else:
                    num3 = num2 * num1
                stack2.append(num3)
                # push

    print("#{} {}".format(tc, stack2[0]))
    # 최종적으로 stack에는 하나의 값만 남는다











