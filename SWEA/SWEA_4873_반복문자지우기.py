import sys
sys.stdin = open("4873.txt", "r")

# 재귀
# new_str이 더이상 if에 해당하지 않는 경우 문자열 반환이 안 됨
def find(str):
    for i in range(len(str)-1):
        if str[i] == str[i+1]:
        # 문자열 s에서 반복된 문자를 지우려고 한다(앞부터 2개씩)
            new_str = str[0:i] + str[i+2:]
            # 지워진 부분은 다시 앞뒤를 연결
            find(new_str)
        return str

T = int(input())
for tc in range(1, T+1):
    str = list(input())

    result = find(str)

    if len(result) != 0:
    # str리스트에 남은 문자열 값이 존재할 때
        print("#{} {}".format(tc, len(result)))
        # 문자열의 길이 반환
    else:
    # 남은 문자가 없는 경우
        print("#{} {}".format(tc, 0))
        # 0을 반환

# stack
T = int(input())

for tc in range(1, T+1):
    Data = list(input())
    N = len(Data)
    stack = []
    for i in range(N):
        if not stack or stack[-1] != Data[i]:
        # stack이 비었거나 (not stack)
        # 스택의 마지막 값이 데이터 내 값과 같지 않은 경우 (stack[-1] != Data[i])
            stack.append(Data[i])
            # stack push
        elif stack and stack[-1] == Data[i]:
        # stack에 값이 있고 (stack)
        # 스택의 마지막 값과 데이터 내 값과 같은 경우 (stack[-1] == Data[i])
            stack.pop()
            # stack pop
            # stack[-1] top을 pop
    print("#{} {}".format(tc, len(stack)))


def find():
# 반복 문자를 지우는 함수
    s = []
    # 문자를 담기위한 스택

    for i in range(len(str)):
    # 문자열 전체에 대해서
        if len(s) != 0:
        # 스택이 비어있지 않으면
            ch = s.pop()
            # 마지막 원소 stack pop
            if str[i] != ch:
            # 같지 않으면
                s.append(ch)
                # 스택에서 꺼내온 문자 stack push
                # 이전에 stack pop해서 원상복귀
                s.append(str[i])
                # 같았다면 stack push
        else:
        # 스택이 비어있으면
            s.append(str[i])
            # 현재 문자 stack push
    return len(s)


T = int(input())
for tc in range(1, T + 1):
    str = input()
    # print(str)
    print("#{} {}".format(tc, find()))