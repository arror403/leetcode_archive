class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g=[[] for _ in range(numCourses)]
        for p in prerequisites:
            g[p[1]].append(p[0])
        
        degrees=[0]*len(g)
        for adj in g:
            for v in adj:
                degrees[v]+=1

        print(degrees)
        for i in range(numCourses):
            j=0
            while(j<numCourses):
                if degrees[j]==0: break
                j+=1

            if j==numCourses: return False

            degrees[j]-=1
            for v in g[j]:
                degrees[v]-=1


        return True