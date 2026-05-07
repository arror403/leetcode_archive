class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        L = len(graph)
        res = []

        def dfs(path, cur):
            if cur==(L-1):
                res.append(path)
            else:
                for i in graph[cur]:
                    dfs(path + [i], i)
            
        dfs([0], 0)


        return res