from collections import deque as dq
row,col=4,5
m = [
    [1, 1, 1, 1, 1],  
    [1, 0, 0, 0, 1],  
    [1, 1, 1, 1, 1],  
    [0, 0, 0, 1, 0]
]
start = (0,0)
end = (2,4)
flags=[1,2,3,4]
d=[(0,1),(1,0),(-1,0),(0,-1)]
q=dq([(start,-1,0)])

while q:
    
    a,b,c=q.popleft()
    if a==end:
        print(c)
        
    
    for z in range(len(d)):
        x,y=d[z][0],d[z][1]
        ci,cj=a[0]+x,a[1]+y
        if 0<=ci<row and 0<=cj<col and m[ci][cj]!=0:
            cnt=c
            mf=-1
            if b==-1 or b==flags[z]:
                mf=flags[z]
            else:
                mf=flags[z]
                cnt+=1
            q.append(((ci,cj),mf,cnt))
print(l)
        


            
                
            
                
                

