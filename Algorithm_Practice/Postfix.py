'''
3
print('{} {}'.format(1, 2))
N, M = map(int, input().split())
print('#{} {}'.format(tc, find())
'''
# 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램
# 정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력

T = int(input())
for tc in range(1, T+1):
    str = input()

    stack = []
    # 스택 빈 리스트 초기값 설정

    for i in range(len(str)):
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
                break
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