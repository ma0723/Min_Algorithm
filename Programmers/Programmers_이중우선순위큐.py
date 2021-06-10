def solution(operations):
    answer = []
    q = []

    for value in operations:
        command, number = value.split()
        if command == 'I':
            # I 숫자 : 숫자 삽입
            q.append(int(number))
        elif command == 'D' and len(q) != 0:
            # D 1 : 최댓값을 삭제
            # D -1 : 최솟값을 삭제
            # 빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시
            if int(number) == 1:
                q.remove(max(q))
                # 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제
            elif int(number) == -1:
                q.remove(min(q))

    if len(q) != 0:
        # 비어있지 않으면 [최댓값, 최솟값]을 return
        answer = [max(q), min(q)]
    else:
        # 모든 연산을 처리한 후 큐가 비어있으면 [0,0]
        answer = [0, 0]
    return answer

# 최소힙 import heapq
# heapq.heappush(heap, value)
# heapq.heappop(heap)
# 최소힙의 최대값 추출 heapq.nlargest(cnt, heap) list반환 유의
# 리스트 값의 인덱스 추출 list.index(value)