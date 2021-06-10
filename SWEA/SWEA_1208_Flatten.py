import sys
sys.stdin = open("1208.txt", "r")

# 버블 정렬
# 카운팅 정렬

def my_max():
    max_height = box_height[0]
    max_index = 0
    # 초기값 index 0인 첫번째 값, 인덱스는 0 설정
    for i in range(len(box_height)):
        if box_height[i] > max_height:
            max_height = box_height[i]
            max_index = i
    return max_index
    # 최소 높이의 위치 인덱스


def my_min():
    min_height = box_height[0]
    min_index = 0
    # 초기값 index 0인 첫번째 값, 인덱스는 0 설정
    for j in range(len(box_height)):
        if box_height[j] < min_height:
            min_height = box_height[j]
            min_index = j
    return min_index
    # 최대 높이의 위치 인덱스


for tc in range(1, 11):
    # 총 10개의 테스트 케이스 반복

    dump = int(input())
    # 덤프 횟수
    box_height = list(map(int, input().split()))
    # 박스 높이

    for k in range(dump):
        # 덤프횟수 반복
        box_height[my_max()] -= 1
        # 최대 높이 위치의 인덱스(my_max())에 접근하여 높이(box_height[my_max()])를 1개 감소
        box_height[my_min()] += 1
        # 최소 높이 위치의 인덱스(my_min())에 접근하여 높이(box_height[my_min()])를 1개 감소

    result = box_height[my_max()] - box_height[my_min()]
    #  최고점과 최저점의 높이 차

    print('#{} {}'.format(tc, result))
    # 출력