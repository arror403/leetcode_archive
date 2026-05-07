class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def bfs_max_level(start):
            """Returns the maximum level achievable from a starting node"""
            visited = set()
            levels = {start: 1}  # Move levels inside this function
            queue = deque([(start, 1)])  # (node, level)
            visited.add(start)
            max_level = 1
            
            while queue:
                node, level = queue.popleft()
                max_level = max(max_level, level)
                
                for next_node in adj[node]:
                    # If node not visited, assign next level
                    if next_node not in visited:
                        visited.add(next_node)
                        levels[next_node] = level + 1
                        queue.append((next_node, level + 1))
                    # If node is visited, check if levels are compatible
                    elif abs(levels[next_node] - level) != 1:
                        return -1
            
            return max_level
        
        def find_component(node):
            """Returns all nodes in the connected component containing the given node"""
            component = []
            visited = set()
            
            def dfs(u):
                visited.add(u)
                component.append(u)
                for v in adj[u]:
                    if v not in visited:
                        dfs(v)
            
            dfs(node)
            return component
        
        # Process each connected component separately
        visited = set()
        total_groups = 0
        
        for node in range(1, n + 1):
            if node not in visited:
                component = find_component(node)
                visited.update(component)
                
                # Try starting from each node in the component
                max_groups = -1
                for start in component:
                    curr_groups = bfs_max_level(start)
                    if curr_groups == -1:  # Invalid grouping found
                        continue
                    max_groups = max(max_groups, curr_groups)
                
                if max_groups == -1:
                    return -1
                total_groups += max_groups
        
        return total_groups


# class Solution:
#     def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
#         adj=[[] for _ in range(505)]
#         col=[0]*505
#         dis=[[0]*505 for _ in range(505)]
#         flag=False
#         kara=[] #nodes in a connected graph
#         res=ind=0

#         #check if graph is bipartite
#         def dfs(u, c=1):
#             col[u]=c
#             kara.append(u)
#             for v in adj[u]:
#                 if not col[v]: dfs(v, 3-c)
#                 elif col[v]==c: flag=False #graph is not bipartite


#         #calculate minimum distance between all nodes
#         def bfs(src):
#             for i in range(1,501): dis[src][i]=100001
#             dis[src][src]=1
#             q=deque()
#             q.append(src)
#             while len(q):
#                 u=q.popleft()
#                 for v in adj[u]:
#                     if (dis[src][v]>dis[src][u]+1):
#                         dis[src][v]=dis[src][u]+1
#                         q.append(v)


#         # for i in range(1,n+1):
#             # adj[i].clear()
#             # adj[i]=[0]*len(adj[i])
#         adj=[[] for _ in range(505)]
            
#         # memset(col,0,sizeof col)
#         col=[0]*505
        

#         for a,b in edges:
#             adj[a].append(b)
#             adj[b].append(a)

#         for i in range(1,n+1):
#             bfs(i)
        
#         for i in range(1,n+1):
#             if col[i]==0:
#                 kara=[0]*len(kara)
#                 flag=True
#                 ind+=1
#                 dfs(i)

#                 if (not flag): return -1

#                 mxdis=0
#                 for i in kara:
#                     for j in kara:
#                         mxdis=max(mxdis,dis[i][j])

#                 res+=mxdis


#         return res