import sys
sys.stdin = open("5207.txt", "r")

# 양쪽 번갈아가는 것 고려안 하면 테케 4개만 통과
# 양쪽 번갈아가지 않고 한쪽만 계속 탐색하는 경우 flag 표시
def partition(a, begin, end):
    pivot = begin
    # 피봇아이템
    L = begin
    R = end
    while L <= R:
        if a[L] <= a[pivot]:
            L += 1
            # 왼쪽 끝에서 pivot으로
            # pivot보다 큰 경우 찾으면 종료
        if a[R] >= a[pivot]:
            R -= 1
            # 오른쪽 끝에서 pivot으로
            # pivot보다 작은 경우 찾으면
        if L < R:
            a[L], a[R] = a[R], a[L]
            # pivot 기준 정렬되지 않은 숫자 교환
    a[pivot], a[R] = a[R], a[pivot]
    return R

def QuickSort(a, begin, end):
    if begin < end:
        pivot = partition(a, begin, end)
        QuickSort(a, begin, pivot-1)
        # 왼쪽
        QuickSort(a, pivot+1, end)
        # 오른쪽

def binarySearch(a, low, high, key, flag):
# 재귀
# a 리스트
# key 탐색키
    global cnt
    if low > high:
        return 0
        # 검색 실패
    else:
        middle = (low+high)//2
        # 중앙값 몫 정수형(//)
        if a[middle] == key:
        # 탐색키를 찾은 경우
            cnt += 1
            return 1
            # 검색 성공
        elif a[middle] > key:
        # 탐색키보다 큰 경우
        # 한쪽 구간을 지속적으로 탐색하면 안 된다 (양쪽 번갈아 가며)
            if flag==1:
                return 0
            else:
                binarySearch(a, low, middle-1, key, 1)
                # 오른쪽 버리고 왼쪽 검색
        elif a[middle] < key:
        # 탐색키보다 작은 경우
        # 한쪽 구간을 지속적으로 탐색하면 안 된다 (양쪽 번갈아 가며)
            if flag==2:
                return 0
            else:
                binarySearch(a, middle+1, high, key, 2)
                # 왼쪽 버리고 오른쪽 검색

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # A와 B에 속한 정수의 개수 N, M
    NList = list(map(int, input().split()))
    MList = list(map(int, input().split()))
    # 두 줄에 걸쳐 N개와 M개의 백만 이하의 양의 정수

    QuickSort(NList, 0, N-1)
    # 리스트, 첫 인덱스, 마지막 인덱스
    # 서로 다른 정수 N개가 주어지면 정렬한 상태로 리스트 A에 저장

    cnt = 0
    for i in range(len(MList)):
    # 리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 이진 탐색을 통해 확인
        if MList[i] in NList:
        # B에 속한 어떤 수가 A에 들어있으면서
            binarySearch(NList, 0, N-1, MList[i], 0)
            # 동시에 탐색 과정에서 양쪽구간을 번갈아 선택하게 되는 숫자의 개수
            # 한쪽 구간을 지속적으로 탐색하면 안 된다

    print("#{} {}".format(tc, cnt))
    # M개의 정수 중 조건을 만족하는 정수의 개수


