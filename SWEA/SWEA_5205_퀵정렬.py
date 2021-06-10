import sys
sys.stdin = open("5205.txt", "r")

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
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 정수의 개수 N
    number = list(map(int, input().split()))
    # 다음 줄에 N개의 정수
    QuickSort(number, 0, len(number)-1)
    print("#{} {}".format(tc, number[N//2]))
    # 퀵 정렬을 구현해 N개의 정수를 정렬해 리스트 A에 넣고
    # A[N//2]에 저장된 값을 출력하는 프로그램
