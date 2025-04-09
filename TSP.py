mp={}
n=int(input("enter number of cities "))
t=0
cities=[]
for i in range(n):
    c=0
    inp=input("enter city ")
    cities.append(inp)
    mp[inp]={}
    for j in range(n):
        x=input(f"enter cities connected to {inp} ")
        if c==t:
            mp[inp][x]=0
        else:
            mp[inp][x]=int(input("distance "))
        c+=1
    t+=1
start=input("enter the start city ")
visited=set(start)
stck=[start]
path=[]
cost=0
while stck:
    z=stck.pop()
    m1,m2="",100
    path.append(z)
    for _ in mp[z]:
        if 0<mp[z][_]<m2 and _ not in visited:
            m1=_
            m2=mp[z][_]
    if m1=="":
        break
    else:
        stck.append(m1)
        visited.add(m1)
        cost+=m2
path.append(start)
cost+=mp[path[-1]][start]
print(path,cost)
        
        
            

