from collections import Counter

n,k=map(int,input().split())
use=list(map(int,input().split()))
if n>=k:
    print(0)
    exit()
    
plug=[]
cnt=0

change=0
maximum=0
for i in range(k):
    if use[i] in plug:
        continue
    if len(plug)<n:
        plug.append(use[i])
        continue
    
    
  
    for j in range(n):
        #change는 플러그에서 뺄 것
        if plug[j] not in use[i:]:
            change=plug[j]
            break
        
        elif use[i:].index(plug[j])>maximum:
            maximum=use[i:].index(plug[j])
            change=plug[j]

    plug[plug.index(change)]=use[i]
    maximum=0
    cnt+=1
print(cnt)
           
