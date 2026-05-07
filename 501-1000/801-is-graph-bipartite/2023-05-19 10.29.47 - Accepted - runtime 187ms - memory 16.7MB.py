class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n  # Colors: 0 (unvisited), 1 and -1 (two different sets)
        
        for i in range(n):
            if color[i] == 0:  # Unvisited vertex
                queue = deque([i])
                color[i] = 1
                
                while queue:
                    curr = queue.popleft()
                    for neighbor in graph[curr]:
                        if color[neighbor] == color[curr]:
                            return False  # Conflict found, not bipartite
                        elif color[neighbor] == 0:
                            color[neighbor] = -color[curr]
                            queue.append(neighbor)
        
        return True  # No conflicts found, bipartite