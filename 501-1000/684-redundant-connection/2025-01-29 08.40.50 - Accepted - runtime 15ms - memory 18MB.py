class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        L=len(edges)
        graph=[[] for _ in range(L+1)]
        for E in edges:
            vis=[False]*(L+1)
            graph[E[0]].append(E[1])
            graph[E[1]].append(E[0])
            if self.dfs(graph, vis, E[0]): return E
        
        return []
        # un-reachable


    def dfs(self, graph, vis, cur, par = -1):
        if vis[cur]: 
            return True    
        # reached already visited node - cycle detected
        vis[cur]=True
        for child in graph[cur]:
            if (child!=par and self.dfs(graph, vis, child, cur)): return True

        return False    
        # no cycle found