# 나이와 이름이 가입한 순서대로
# 나이가 증가하는 순으로
# 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬(가입순서 원래 인덱스)
# 딕셔너리 구조

# 첫째 줄부터 총 N개의 줄에 걸쳐
# 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로
# 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력

import sys
n = int(sys.stdin.readline())
member = []
for i in range(n):
    member.append(list(sys.stdin.readline().split()))
member.sort(key=lambda x: int(x[0]))
# lamda 기준 정렬
# 원래 정렬 순서가 가입순서이므로 나이가 같은 경우 알아서 가입순 정렬
for i in range(n):
    print(member[i][0], member[i][1])