def solution(answers):
    answer = []
    person = [0, 0, 0]
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if answers[i] == pattern1[i%len(pattern1)]:
        # [0] == [5]
        # [1] == [6]
            person[0] += 1
        if answers[i] == pattern2[i%len(pattern2)]:
            person[1] += 1
        if answers[i] == pattern3[i%len(pattern3)]:
            person[2] += 1
    print(person)
    if person.count(max(person)) > 1:
    # 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬
    # list.count(value)
        for i in range(len(person)):
            if person[i] == max(person):
                answer.append(i+1)
                answer.sort()
                # 오름차순 정렬
                # list.sort()
    else:
    # 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return
        answer.append(person.index(max(person))+1)
        # 인덱스 반환 list.index(value)
    return answer