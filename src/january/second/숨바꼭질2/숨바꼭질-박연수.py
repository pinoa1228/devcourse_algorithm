from collections import deque

n,k=map(int,input().split())

q=deque()
q.append(n)
# 메모리 초과 방지하기 위해 그 곳에 가기까지의 최소비용을 저장하는 배열을 만든다.
visited=[0]*100001
visited[n]=0

def go(number,position):
    if number==0:
        return position+1
    elif number==1:
        return position-1
    else:
        return position*2

def bfs():
    global min_time,cnt
    while q:
        x=q.popleft()  
        time=visited[x]
        if x==k:
            min_time=time
            cnt+=1
            continue                            
        for i in range(3):
            new_x=go(i,x)
            if new_x<0 or new_x>=100001:
                continue
            #방문한적 없거나,현재시간+1보다 큰 경우
            if visited[new_x]==0 or visited[new_x]==visited[x]+1:
                visited[new_x]=time+1
                q.append(new_x)

min_time=1e9
cnt=0
bfs()
print(min_time)
print(cnt)