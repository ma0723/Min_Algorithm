from itertools import permutations

# ord() chr() 아스키코드 함수 26개 소문자, 26개 대문자

# 찾고자 하는 단어 W의 길이 g
# 발굴된 벽화에서 추출한 문자열 S의 길이 |S|가 빈 칸

# 둘째 줄에 W
# 셋째 줄에 S의 실제 내용

# 첫째 줄에 W의 순열이 S 안에 있을 수 있는 형태의 개수
# 문자열 탐색
# w의 모든 순열을 s와 비교하는 방식으로 풀었지만 시간초과
# 순열, 조합

n, m = map(int, input().split())
w = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()

wl = [0] * 52
sl = [0] * 52
# 각 글자 카운팅 정렬

# w의 각 알파벳마다 등장하는 부분 +1
for i in range(n):
# w의 길이만큼 순회
    if 'a' <= w[i] <= 'z':
        wl[ord(w[i]) - ord('a')] += 1
        # 각 소문자 카운팅 정렬 추가
    else:
        wl[ord(w[i]) - ord('A') + 26] += 1
        # 각 대문자 카운팅 정렬 추가

start, length, count = 0, 0, 0

for i in range(m):
    if 'a' <= s[i] <= 'z':
        sl[ord(s[i]) - ord('a')] += 1
    else:
        sl[ord(s[i]) - ord('A') + 26] += 1
    length += 1

    if length == n:
        if wl == sl:
            count+=1
        if 'a' <= s[start] <= 'z':
            sl[ord(s[start]) - ord('a')] -= 1
        else:
            sl[ord(s[start]) - ord('A') + 26] -= 1
        start += 1
        # 위치 비교 인덱스 1씩 이동
        length -= 1
        # 비교할 길이 n에서 n-1개의 순열...1개의 순열로 줄어든다


print(count)