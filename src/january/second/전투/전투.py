n,m=map(int,input().split())

graph=[]

for _ in range(m):
    graph.append(list(input()))
    
dx=[-1,1,0,0]
dy=[0,0,-1,1]

visited=[[False]*n for _ in range(m)]

# 전력 결과를 담기 위한 dictionary
dict={"W":0,"B":0}

def dfs(x,y,target):
    global cnt
    visited[x][y]=True
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        
        if nx<0 or nx>=m or ny<0 or ny>=n:
            continue
        if not visited[nx][ny] and graph[nx][ny]==target:
            cnt+=1
            dfs(nx,ny,target)
        
        
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            cnt=1
            dfs(i,j,graph[i][j])
            dict[graph[i][j]]+=cnt**2

print(dict["W"],dict["B"])
        