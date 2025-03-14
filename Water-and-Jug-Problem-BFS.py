from collections import deque as dq
class Solution:
    def canMeasureWater(self, x: int, y: int, t: int) -> bool:
        def shift(a,b,ax):
            cp=ax-a
            z=min(cp,b)

            return (a+z,b-z)

        stck=dq([(0,0)])
        st=set((0,0))
        while stck:
            m,n=(0,0),(0,0)
            p,q=stck.popleft()

            if p==t or q==t or p+q==t:
                return True
            
            if (x,q) not in st:
                stck.append((x,q))
                st.add((x,q))
            if (p,y) not in st:
                st.add((p,y))
                stck.append((p,y))
            if (0,q) not in st:
                st.add((0,q))
                stck.append((0,q))
            if (p,0) not in st:
                st.add((p,0))
                stck.append((p,0))

            if p<q:
                v=shift(p,q,x)
                m=(v[0],v[1])
            if q<p:
                v=shift(q,p,y)
                n=(v[1],v[0])
            if m not in st:
                stck.append(m)
                st.add(m)
            if n not in st:
                stck.append(n)
                st.add(n)
        return False



