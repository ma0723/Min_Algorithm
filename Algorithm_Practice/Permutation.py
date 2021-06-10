def perm(k):    
# k : 선택한 원소가 들어갈 자리(sel)
    if k == N:     
    # 원소선택이 끝나면
        print(sel) 
        # 출력
        return
        # 재귀함수 다시 호출 
    for i in range(N):  
    # 모든 원소 순회
        if visited[i] == 0:     
        # 선택하지 않은 경우
            sel[k] = arr[i]     
            # arr[i]원소를 선택해서 k번째에 위치함
            visited[i] = 1      
            # 선택 표시
            perm(k+1)
            # 재귀함수 호출
            visited[i] = 0
            # return한 후에는 선택 표시 해제

arr = [1,2,3]   
# 순열을 만들기 위한 원소
N = len(arr)    
# 순열의 길이
sel = [0] * N        
# 만들어진 순열 저장  
# 1,2,3 / 1,3,2..
visited = [0] * N       
# 선택여부 저장      
# 0,0,1
perm(0)
# 시작 0으로 입력