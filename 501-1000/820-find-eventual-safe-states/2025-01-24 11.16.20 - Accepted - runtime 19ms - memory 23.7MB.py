class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = [0] * len(graph)

        def dfs(start, color):
            if color[start]!=0:
                return color[start]==1
            
            color[start]=2
            for newNode in graph[start]:
                if not dfs(newNode, color):
                    return False

            color[start]=1

            return True
        
        
        return [i for i in range(len(graph)) if dfs(i, color)]