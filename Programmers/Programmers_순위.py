def solution(n, results):
# 선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수
    answer = 0
    # 순위를 매길 수 있는 사람
    win = {}
    lose = {}
    for i in range(1, n+1):
        win[i] = set()
        lose[i] = set()
        # 시간초과시 set()을 값으로 설정
    results.sort()
    # 번호순서대로 정렬
    for i in range(1, n+1):
    # 각각 1번부터 n번까지 번호
        for result in results:
        # 결과 2차원 배열 순회
            if result[0]==i:
                win[i].add(result[1])
                # [A, B]는 A 선수가 B 선수를 이겼다
            if result[1]==i:
                lose[i].add(result[0])
                # [A, B]는 B 선수가 A 선수에게 졌다
        for j in win[i]:
        # i에게 진 상대들(j)을 순회하며
            lose[j].update(lose[i])
            # j는 i에게 진 상대들에게는 다 진 것
        for j in lose[i]:
        # i에게 이긴 상대들(j)을 순회하며
            win[j].update(win[i])
            # j는 i가 이긴 상대들은 다 이긴 것
    for i in range(1, n+1):
    # 각각 1번부터 n번까지 번호
        if len(win[i]) + len(lose[i]) == n-1:
        # 이긴 횟수 + 진 횟수 = n-1 (순위 가능)
            answer += 1
    return answer