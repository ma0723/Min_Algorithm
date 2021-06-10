import sys
sys.stdin = open("1240.txt", "r")

code_dic = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9,
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 세로 크기 N, 배열의 가로크기 M
    lst = [list(map(int, input())) for _ in range(N)]
    # print(lst)

    result = []
    for i in range(N):
    # 행 우선 조회
        for j in range(M-1, -1, -1):
        # 열 역순 조회
            password = ''
            if lst[i][j] == 1:
            # 암호는 항상 마지막이 1로 끝난다
                for k in range(6, -1, -1):
                # 암호코드에 구성하는 숫자 하나가 차지하는 길이는 7칸
                    password += str(lst[i][j-k])
                    # lst[i][j-6] .. lst[i][j]
                    # 모든 암호코드는 8개의 숫자로 구성
                    # 암호코드의 가로 길이는 총 길이는 56칸
                    lst[i][j-k] = 0
                    # 초기화
                result.append(password)
                # print(password)
                # 암호 뒷부분부터 저장
                # 순회 역순 유의
        if len(result)==8:
        # 암호 8개를 찾은 경우
            break
            # 행 우선 조회 for문 종료

    ans = []
    for password in result:
        try:
            number = code_dic[password]
            # 정상적인 암호코드들을 판별한 뒤
            # 딕셔너리에 key가 존재하지 않는 경우 비정상 암호코드 판별
            ans.append(number)
            # 암호 뒷부분부터 저장
            # 순회 역순 유의
        except:
            ans = []
            pass

    ans = ans[::-1]
    # 순회 역순 유의
    total = 0
    for i in range(len(ans)):
        if i%2==0:
        # 홀수 자리의 합 x 3
        # 인덱스0 1번째 홀수번쨰
            total += 3*ans[i]
        else:
        # 짝수 자리의 합
            total += ans[i]
    # print(total)

    if total%10 != 0:
    # 모든 암호코드가 정상적인 암호코드임을 보장할 수 없다
    # 10의 배수가 아닌 경우    
        print("#{} {}".format(tc, 0))
    if total%10==0:
    # 10의 배수인 경우
        my_sum = 0
        for i in ans:
            my_sum += i
        print("#{} {}".format(tc, my_sum))
        # 정상적인 암호코드들을 판별한 뒤 이 암호코드들에 적혀있는 숫자들의 합을 출력