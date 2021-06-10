from collections import deque

answer = 0


# global로 변경

def solution(priorities, location):
    # 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치 location
    global answer
    wait = deque([])
    # 큐 생성
    for i in range(len(priorities)):
        wait.append([priorities[i], i])
        # [우선순위 값, 인덱스 위치] 추가
    find(wait, priorities, location)
    return answer


def find(q, lst, target):
    global answer
    while q:
        value = q.popleft()
        # 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록
        priority = value[0]
        # 우선순위 값
        idx = value[1]
        # 찾고자 하는 target을 알파벳대신 인덱스 숫자로 별도 표기
        if priority < max(lst):
        # 나머지 인쇄 대기목e)
        # J를 대기목록의 가장 마지막에 넣습니다
        else:
            # 그렇지 않으면 J를 인쇄
            answer += 1
            # 인쇄 횟수 1씩 증가
            lst.remove(priority)
            # 우선순위 값 리스트 해당값 제거
            if idx == target:
                # 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return
                break
                # location target을 찾으면 while문 종료