import sys
sys.stdin = open("4866.txt", "r")

# 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램
# 정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력

T = int(input())
for tc in range(1, T+1):
    str = input()

    stack = []
    # 스택 빈 리스트 초기값 설정

    for i in range(len(str)):
    # 문자열의 길이만큼 인덱스에 접근하며 탐색
        if str[i] == '(' or str[i] == '{':
        # 여는 괄호일 경우
            stack.append(str[i])
            # stack push
        elif str[i] == ')' or str[i] == '}':
        # 닫는 괄호일 경우
            if len(stack) == 0:
            # 빈 스택에 닫는 괄호부터 먼저 온 경우
                stack = [str[i]]
                break
                # 괄호 검사 실패 i for문 종료
            elif (str[i] == "}" and stack[-1] != "{") or (str[i] == ")" and stack[-1] != "("):
            # stack에 저장된 마지막 값이 일치하지 열린 괄호가 아닌 경우(stack[-1] != "{")(stack[-1] != "(")
            # 가장 마지막 인덱스의 값 stack[-1]
                stack = [str[i]]
                # stack push
                break
                # 괄호 검사 실패 i for문 종료
            else:
            # stack에 저장된 마지막 값이 닫는 괄호와 일치하는 열린 괄호가 오는 경우
                stack.pop()
                # 가장 마지막 인덱스 제거

    if not len(stack):
    # stack의 길이가 0인 경우(괄호 검사 이후 모두 pop)
        print(f'#{tc} 1')
    else:
    # stack에 남은 값이 존재하는 경우(괄호 검사 이후 모두 pop하지 못한 경우)
        print(f'#{tc} 0')

def find():
# 괄호검사 함수
    for i in range(len(str)):
    # 문자열의 길이만큼 문자열의 인덱스에 접근하여 탐색하면서
        if str[i] == '(' or str[i] == '{' :
        # 시작괄호
            s.append(str[i])
            # stack push
        elif str[i] == ')' or str[i] == '}' :
        # 닫는 괄호
            if not s:
            # 스택이 비어있으면 if len(s) == 0:
                return 0
                # 함수 for문 종료 return
            r = s.pop()
            # stack pop
            # stack[-1]인 top을 pop
            if (str[i] == "}" and r == "(") or (str[i] ==')' and r =='{'):
            # stack에서 top을 pop한 값과 괄호의 짝이 맞지 않으면
                return 0
                # 함수 for문 종료 return
    if len(s) == 0:
    # 검사를 다하고 스택에 남은게 없다면 1
        return 1
    else:
    # 스택에 남은게 있다면 0
        return 0


T= int(input())
for tc in range(1,T+1):
    str = input()
    # 문자열로 읽어오기
    # print(str)
    s = []
    # 괄호 검사를 위한 스택
    print("#{} {}".format(tc, find()))