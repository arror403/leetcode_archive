class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        UF={}

        def find(x):
            if x not in UF:
                UF[x]=x
            if x!=UF[x]:
                UF[x]=find(UF[x])

            return UF[x]
        

        def union(x, y):
            rootX=find(x)
            rootY=find(y)
            UF[rootX]=rootY
        

        def BFS(node):
            q=deque([(node,1)])
            seen={node:1}
            level=1
            while q:
                cur,level=q.popleft()
                for nei in graph[cur]:
                    if nei not in seen:
                        seen[nei]=level+1
                        q.append((nei,level+1))
                    elif seen[nei]==level: 
                        return -1

            return level
        

        graph=defaultdict(list)
        for s,e in edges:
            graph[s].append(e)
            graph[e].append(s)
            union(s,e)
        
        maxGroup=defaultdict(int)
        for i in range(1,n+1):
            groups=BFS(i)
            if groups==-1: return -1
            root=find(i)
            maxGroup[root]=max(maxGroup[root],groups)


        return sum(maxGroup.values())