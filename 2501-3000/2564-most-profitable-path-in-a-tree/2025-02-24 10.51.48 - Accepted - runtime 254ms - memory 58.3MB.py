class Solution:
    def mostProfitablePath(self, e: List[List[int]], bob: int, a: List[int]) -> int:
        n = len(a)
        g = [[] for _ in range(n)]
        for u,v in e: g[u].append(v); g[v].append(u)
        d = [n]*n
        def dfs(u, p, t):
            d[u] = 0 if u==bob else n
            r = x = -float('inf')
            for v in g[u]:
                if v != p:
                    r = max(r, dfs(v, u, t+1))
                    d[u] = min(d[u], d[v]+1)
            v = a[u] if d[u]>t else a[u]//2 if d[u]==t else 0
            return v if r==-float('inf') else v+r
        return dfs(0, -1, 0)