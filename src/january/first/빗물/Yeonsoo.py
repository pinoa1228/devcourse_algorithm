h,w=map(int,input().split())
arr=list(map(int,input().split()))

result=0

#맨 오른쪽과 왼쪽은 탐색할 필요가 없기 때문에 1부터 w-1을 탐색해준다.
for i in range(1,w-1):
    #왼쪽에서 제일 큰 블록을 구함
    left=max(arr[:i])
    #오른쪽에서 제일 큰 블록을 구함
    right=max(arr[i+1:])
    # 왼쪽과 오른쪽에서 작은 값만큼 빗물이 담길 수 있다.
    m=min(left,right)
    
    # 현재 블록의 수보다 m이 클때만 빗물이 담길 수 있다.
    if m>arr[i]:
        result+=m-arr[i]

print(result)
