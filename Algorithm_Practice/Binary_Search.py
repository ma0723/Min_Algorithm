from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
# 정렬 필수
# 두 함수는 '정렬된 리스트'에서 '값이 특정 범위에 속하는 원소의 개수'를 구하고자 할 때
x = 4

print(bisect_left(a, x))
# 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
print(bisect_right(a, x))
# 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드