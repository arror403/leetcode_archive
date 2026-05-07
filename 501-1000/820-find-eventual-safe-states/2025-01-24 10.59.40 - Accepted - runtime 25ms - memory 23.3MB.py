class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        if not graph: return res

        color = [0] * len(graph)
        
        return [i for i in range(len(graph)) if self.dfs(graph, i, color)]


    def dfs(self, g, start, color):
        if color[start] != 0: return color[start] == 1
        
        color[start] = 2
        for newNode in g[start]:
            if not self.dfs(g, newNode, color):
                return False

        color[start] = 1
        
        return True