class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        c=0
        def dfs(m,nod):
            di=[(0,1),(1,0),(-1,0),(0,-1)]
            stck=[nod]

            while stck:

                a=stck.pop()

                for i,j in di:
                    ci,cj=a[0]+i,a[1]+j
                    
                    if 0<=ci<len(m) and 0<=cj<len(m[0]) and m[ci][cj]=='1':
                        stck.append((ci,cj))
                        m[ci][cj]='#'

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    dfs(grid,(i,j))
                    c+=1
        return c





            
        
