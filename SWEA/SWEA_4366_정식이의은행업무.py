import sys
sys.stdin = open("4366.txt", "r")

def find(second_number, third_number): 
# 2진수 반전 / 3진수 반전 -> 10진수 변환 -> 같은 경우
    second_lst = []
    for i in range(len(second_number)):
        change_num = [i for i in second_number]
        # 값 변경을 위해 복제
        # 2진수의 각 자리를 1 혹은 0 반전 모든 경우 list
        for j in range(2):
            if change_num[i] != j:
                change_num[i] = j
            second_lst.append(second(change_num))
    third_lst = []
    for i in range(len(third_number)):
        change_num = [i for i in third_number]
        # 값 변경을 위해 복제
        # 3진수의 각 자리를 2, 1, 혹은 0 반전 모든 경우 list
        for j in range(3):
            if change_num[i] != j:
                change_num[i] = j
            third_lst.append(third(change_num))
    for i in second_lst:
        for j in third_lst:
            if i==j:
            # 각 list의 같은 값 탐색
                return i

def second(num):
# 이진수를 십진수로 전환하는 함수
    result = 0
    for i in range(len(num)):
        result += num[i]*(2**(len(num)-i-1))
    return result

def third(num):
# 삼진수를 십진수로 전환하는 함수
    result = 0
    for i in range(len(num)):
        result += num[i] * (3 ** (len(num) - i - 1))
    return result

T = int(input())
for tc in range(1, T+1):
    second_number = [int(i) for i in input()]
    third_number = [int(i) for i in input()]
    # 2진수와 3진수 각각의 수에서 단 한 자리만을 잘못 기억하고 있다는 것

    find(second_number, third_number)
    # 2진수의 각 자리를 1 혹은 0 반전 모든 경우 list
    # 3진수의 각 자리를 2, 1, 혹은 0 반전 모든 경우 list
    # 각 list의 같은 값 탐색

    print("#{} {}".format(tc, find(second_number, third_number)))