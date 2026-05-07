class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        def dfs(al, visited, s):
            change=0
            visited[s]=True
            for to in al[s]:
                if not visited[abs(to)]:
                    change+=dfs(al, visited, abs(to))+(to>0)
            return change

        al=[[] for _ in range(n)]
        for c in connections:
            al[c[0]].append(c[1])
            al[c[1]].append(-c[0])


        return dfs(al, [False]*n, 0)