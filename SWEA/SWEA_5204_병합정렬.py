import sys
sys.stdin = open("5204.txt", "r")

# 시간초과 (슬라이싱/pop)
# def merge(left, right):
# # 병합단계
#     global cnt
#     if left[-1] > right[-1]:
#     # 병합 과정에서 다음처럼 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력
#     # 오른쪽 원소가 먼저 복사되는 경우의 수
#         cnt += 1
#     result = []
#     while len(left) > 0 or len(right) > 0:
#         if len(left) > 0 and len(right) > 0:
#             if left[0] <= right[0]:
#                 result.append(left[0])
#                 left = left[1:]
#             else:
#                 result.append(right[0])
#                 right = right[1:]
#         elif len(left) > 0:
#             result.extend(left[0:])
#             break
#         elif len(right) > 0:
#             result.extend(right[0:])
#             break
#     return result

# 런타임에러 10개 중 9개 테스트케이스 통과
# 변수 l, r에서 l이 문제 -> 변수 i, j로 수정
def merge(left, right):
# 병합단계
    global cnt
    if left[-1] > right[-1]:
    # 병합 과정에서 다음처럼 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력
    # 오른쪽 원소가 먼저 복사되는 경우의 수
        cnt += 1
    i, j = 0, 0
    # 인덱스
    result = []
    while len(left) > i or len(right) > j:
        if len(left) > i and len(right) > j:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif len(left) > i:
            result.extend(left[i:])
            i = len(left)
        elif len(right) > j:
            result.extend(right[j:])
            j = len(right)
    return result

def merge_sort(lst):
# 분할단계
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    LeftList = lst[:mid]
    RightList = lst[mid:]
    # 분할

    LeftList = merge_sort(LeftList)
    RightList = merge_sort(RightList)
    # 정렬

    return merge(LeftList, RightList)
    # 병합

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    print("#{} {} {}".format(tc, merge_sort(lst)[N//2], cnt))
    # N//2 번째 원소와 오른쪽 원소가 먼저 복사되는 경우의 수를 출력
