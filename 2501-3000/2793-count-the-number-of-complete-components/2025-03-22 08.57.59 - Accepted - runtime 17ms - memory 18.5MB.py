class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * n
        res = 0
        
        def dfs(node, component):
            visited[node] = True
            component.append(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor, component)
        
        for i in range(n):
            if not visited[i]:
                component = []
                dfs(i, component)
                
                # Check if component is complete
                is_complete = True
                size = len(component)
                
                # Each node should have exactly (size-1) connections
                for node in component:
                    if len(adj[node]) != size - 1:
                        is_complete = False
                        break
                
                if is_complete:
                    res += 1
        
        return res

# class Solution:
#     def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
#         con=[[0]*n for _ in range(n)]

#         for e in edges:
#             con[e[0]].append(e[1])
#             con[e[1]].append(e[0])

#         mark=[False]*n
#         res=0
#         for i in range(n):
#             if not mark[i]:
#                 x=y=0
#                 self.dfs(i, con, mark, x, y)
#                 res+=int((x*(x-1))==y)


#         return res


#     def dfs(self, x, con, mark, a, b):
#         if mark[x]: return
#         mark[x]=True
#         a+=1
#         b+=len(con[x])
#         for y in con[x]: self.dfs(y, con, mark, a, b)