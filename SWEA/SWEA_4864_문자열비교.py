import sys
sys.stdin = open("4864.txt", "r")

def BruteForce(p, t):
    M = len(p)
    N = len(t)
    for i in range(N-M+1):
    # t의 인덱스는 시작점은 0부터 N-M까지의 인덱스까지
    # 한 칸씩 이동하며 비교
        cnt = 0
        # p와 t의 값이 일치하는 개수 초기값 설정
        for j in range(M):
        # p의 인덱스는 언제나 0부터 len(p)-1까지
            if t[i+j] == p[j]:
            # t의 인덱스는 0부터 j칸만큼 이동하면서 비교
                cnt += 1
                # 일치하는 개수
            else:
                break
                # 같지 않으면 j for문 종료
                # 시작점 i for문으로 다시 복귀
        if cnt == M:
        # 일치하는 개수가 p의 길이와 같다면
            return 1
            # 존재하면 1 (검색 성공)
    return 0
    # 존재하지 않으면 0 (검색 실패)

T = int(input())
for tc in range(1, T+1):
    p = input()
    t = input()

    result = BruteForce(p, t)

    print("#{} {}".format(tc, result))



