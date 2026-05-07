class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x,y=0,0
        visited=[[0,0]]
        for i in path:
            if i =='N':
                y+=1
            elif i=='S':
                y-=1
            elif i=='E':
                x+=1
            elif i=='W':
                x-=1
            
            if [x,y] in visited: 
                return True
            else:
                visited.append([x,y])
            
        return False