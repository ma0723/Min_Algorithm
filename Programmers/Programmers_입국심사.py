def solution(n, times):
    # 입국심사를 기다리는 사람 수 n
    # 한 명을 심사하는데 걸리는 시간이 담긴 배열 times
    answer = 0

    left = 1
    # 최소 시간
    right = n * max(times)
    # 최대 시간

    while left <= right:
        mid = (left + right) // 2
        people = 0

        for time in times:
            people += mid // time
            # 설정된 시간동안 각 심사대 처리 사람수
            if people >= n:
                # n명이 넘어가면
                answer = mid
                right = mid - 1
                # mid 중간값보다 작은 값 탐색
                break
                # 시간초과 방지
                # for문 종료
        if people < n:
            # for문을 모두 순회하고 처리한 사람이 n명이 충족하지 못하면
            left = mid + 1
            # mid 중