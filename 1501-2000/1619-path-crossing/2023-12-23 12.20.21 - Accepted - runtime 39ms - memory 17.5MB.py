class Solution:
    def isPathCrossing(self, path: str) -> bool:
        p=[0,0]
        visited=[[0,0]]
        for i in path:
            if i =='N':
                p[1]+=1
            elif i=='S':
                p[1]-=1
            elif i=='E':
                p[0]+=1
            elif i=='W':
                p[0]-=1
            
            # print(p)
            if p in visited: return True
            visited.append(p[:])
            # print(visited)
            
        # print(visited)
        return False