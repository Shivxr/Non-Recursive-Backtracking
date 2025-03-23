row,col=4,5
m = [
    [1, 1, 1, 1, 1],  
    [1, 0, 0, 0, 1],  
    [1, 1, 1, 1, 1],  
    [0, 0, 0, 1, 0]
]
l=[]
start = (0,0)
end = (2,4)
flags=[1,2,3,4]
d=[(0,1),(1,0),(-1,0),(0,-1)]
stck=[(start,-1,0,{(0,0)})]



while stck:
    
    a,b,c,st=stck.pop()
    if a==end:
        l.append(c)
        continue
        
    
    for z in range(len(d)):
        x,y=d[z][0],d[z][1]
        ci,cj=a[0]+x,a[1]+y
        if 0<=ci<row and 0<=cj<col and m[ci][cj]!=0 and (ci,cj) not in st:
            cnt=c
            mf=-1
            if b==-1 or b==flags[z]:
                mf=flags[z]
            else:
                mf=flags[z]
                cnt+=1
            stck.append(((ci,cj),mf,cnt,st | {(ci,cj)}))
print(l)
        


            
                
            
                
                

