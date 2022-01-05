n,k=map(int,input().split())
    
if k<5:
    print(0)
    exit()
elif k==26:
    print(n)
    exit()
    
arr=[]
answer=0
learn=[0]*26
for _ in range(n):
    arr.append(list(set(input())))

# 앞뒤로 붙은 단어에 포함된 알파벳은 배워야한다.
for c in('a','c','i','n','t'):
    learn[ord(c)-ord("a")]=True

def dfs(index,cnt):
    global answer
    
    if cnt==k-5:
        readcnt=0
        for word in arr:
            for w in word:
                check=True
                if not learn[ord(w)-ord('a')]:
                    check=False
                    break
            if check:
                readcnt+=1

        answer = max(answer, readcnt)
        return

# 백트래킹을 이용하여 나머지 배울 알파벳을 탐색
    for i in range(index, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False

dfs(0,0)
print(answer)

                    


        
            
        

