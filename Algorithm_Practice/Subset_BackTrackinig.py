#s: 선택된 원소들의 합
#r:남은 원소들의 합(선택가능한 것들중에)
def f(i, N, K,s, r ):
    global cnt
    if s == K:
    # 부분집합의 원소의 합이 K인 것을 찾음
        cnt+=1
        return
        # 이미 K를 찾았으므로 원소가 추가되면 K보다 커지므로 고려 X
    elif i == N:
    # 모든 원소를 고려함 K는 못찾아냄
        return
    elif s > K:
    # 현재까지의 합이 K보다 커지는 경우
        return
    elif s + r < K :
    # 남은 원소를 모두 포함해도 K가 안되는 경우
        return
    else:
        f(i+1,N,K,s,r-(i+1))
        # i번째 원소를 선택하지 않은 경우
        f(i+1,N,K,s+(i+1),r-(i+1))
        # i번째 원소 선택

cnt = 0
N = 10  #1에서부터 N까지 집합의 원소
K = 10  #부분집합의 합
f(0,N,K,0, (N+1) * N //2 )   #선택된 원소의 합, 아직 선택되지 않은 원소의 합
print(cnt)