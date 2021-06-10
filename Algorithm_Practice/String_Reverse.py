# s = input()
# s = input().split()
# 공백을 기준으로 분리
# 문자열 모두 1개의 값
# 리스트로 출력
# s = list(input())
# 각 문자 모두 len()의 개수만큼 한글자당 값
# 리스트로 출력

#1 for문
s = 'Reverse this string'
s_rev = ''
# 빈 문자열 초기값 설정
for ch in s:
    print(ch)
    s_rev = ch + s_rev
    # ch(나중에) + s_rev(먼저)
    # 순서 유의
print(s_rev)

#2 리스트
s = 'Reverse this string'
s_list = list(s)
# s_list(객체)에 리스트 복사
s_list.reverse()
# list의 reverse 메소드
print(''.join(s_list))
# ''.join()
# ''문자열 객체 반환
# .을 붙이면 메소드 검색 가능

#3 str
s = 'Reverse this string'
print(''.join(reversed(s)))

#4 slicing
s = 'Reverse this string'
print(s[::-1])
# print(s[:])
# 그대로 출력
# [시작:끝(포함안함):방향(-1 반대로)]

#5 list index for문
s = list(input())
print(s)
for i in range(len(s)//2):
    s[i], s[len(s)-i] = s[len(s)-i], s[i]
print(s)