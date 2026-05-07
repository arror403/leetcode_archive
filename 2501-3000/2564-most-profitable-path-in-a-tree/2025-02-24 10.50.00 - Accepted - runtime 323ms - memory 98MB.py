class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        disFromBob = [n] * n
        

        @lru_cache(None)
        def dfs(u: int, par: int, depth: int) -> int:
            ret = 0
            disFromBob[u] = 0 if u == bob else n
            maxChild = -inf
            
            for v in adj[u]:
                if v == par:
                    continue
                maxChild = max(maxChild, dfs(v, u, depth + 1))
                disFromBob[u] = min(disFromBob[u], disFromBob[v] + 1)
            
            if disFromBob[u] > depth:
                ret += amount[u]
            elif disFromBob[u] == depth:
                ret += amount[u]//2
                
            return ret if maxChild == -inf else ret + maxChild
        
        
        return dfs(0, -1, 0)