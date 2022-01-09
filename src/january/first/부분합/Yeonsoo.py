n,s=map(int,input().split())
numberlist=list(map(int,input().split()))

answer=100001
    
start=0
end=0
total=0

while True:
    
    #전체 합보다 클때 전체 길이가 작은 단위로 되어있는지 확인
    if total>=s:
        answer=min(end-start,answer)
        total-=numberlist[start]
        start+=1
    elif end==n:
        break
    else:
        total+=numberlist[end]
        end+=1

if answer==100001:
    print(0)
else:      
    print(answer)

