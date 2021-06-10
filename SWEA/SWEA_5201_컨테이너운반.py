import sys
sys.stdin = open("5201.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 컨테이너 수 N과 트럭 수 M
    luggages = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    # 다음 줄에 N개의 화물이 무게wi, 그 다음 줄에 M개 트럭의 적재용량 ti
    visited = [0] * M
    # 방문 배열

    ans = 0
    # 옮겨진 화물의 전체 무게
    # 컨테이너를 한 개도 옮길 수 없는 경우 0을 출력
    for i in range(M):
    # 트럭의 적재용량 순회
        result = 0
        # 가장 무거운 화물 값 저장
        for luggage in luggages:
        # 화물의 무게 순회
            if trucks[i] >= luggage and luggage >= result:
            # 트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없다 (trucks[i] >= luggage)
            # 화물의 총 중량이 최대가 되기 위해 갱신 (luggage >= result)
                result = luggage
                # 트럭당 한 개의 컨테이너를 운반 가능
        if result != 0:
        # 화물을 싣지 못한 트럭이 있을 수도 있고, 남는 화물이 있을 수도 있다
        # 화물을 싣는 경우
            luggages.remove(result)
            # 옮겨야 하는 화물의 무게 list에서 제거
        ans += result
        # 옮겨진 화물의 전체 무게가 얼마인지 출력

    print("#{} {}".format(tc, ans))
    # 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면 결과
