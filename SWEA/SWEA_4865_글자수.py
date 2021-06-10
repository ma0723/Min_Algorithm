import sys
sys.stdin = open("4865.txt", "r")

T = int(input())
for tc in range(1, T+1):
    p = [i for i in input()]
    p = set(p)
    # 중복 제거 str1
    t = [i for i in input()]
    # str1, str2 각 글자를 리스트로 저장

    result = {}
    # 딕셔너리 이용 가능
    # key 값 저장
    # value 개수 저장
    for i in range(len(t)):
    # t의 인덱스 순회하는 for문
        for j in p:
        # p의 값을 순회하는 for문
            if t[i] == j:
                if t[i] in result.keys():
                # 이미 t[i]의 값인 문자가 result(dictionary)의 key로 존재하는 경우
                    result[t[i]] += 1
                else:
                # t[i]의 값인 문자가 result(dictionary)의 key로 존재하지 않는 경우
                    result[t[i]] = 1

    ans = 0
    # 초기값 설정
    for i in result.values():
    # t의 문자열 중 p의 문자열이 속한 개수 값(.values())
        if ans < i:
            ans = i
            # 최대값 갱신

    print("#{}".format(tc), end = " ")
    print(ans)



