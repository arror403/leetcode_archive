class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        depths = [-1] * n
        reverse_graph = [[] for _ in range(n)]
        for i, v in enumerate(favorite): reverse_graph[v].append(i)
        free_component_total = 0
        
        def dfs_arm_length(node):
            if depths[node] != -1:
                return depths[node]
            
            max_depth = 0
            for neighbor in reverse_graph[node]:
                max_depth = max(max_depth, dfs_arm_length(neighbor))
            
            depths[node] = 1 + max_depth
            return depths[node]

        for i in range(n):
            if depths[i] != -1:
                continue
            
            if favorite[favorite[i]] == i:
                depths[i] = depths[favorite[i]] = 0
                
                arm1_length = max(
                    (dfs_arm_length(v) for v in reverse_graph[i] if v != favorite[i]), default=0)
                
                arm2_length = max(
                    (dfs_arm_length(v) for v in reverse_graph[favorite[i]] if v != i), default=0)
                
                free_component_total += arm1_length + arm2_length + 2

        def dfs_cycle_length(node):
            if depths[node] != -1:
                return (node, depths[node], False)
            
            depths[node] = 0
            entry_point, depth, cycle_visited = dfs_cycle_length(favorite[node])
            
            if cycle_visited:
                return (entry_point, depth, True)
            
            depths[node] = 1 + depth
            return (entry_point, depths[node], node == entry_point)
        
        max_cycle_length = 0
        for i in range(n):
            if depths[i] != -1:
                continue
            
            _, depth, cycle_visited = dfs_cycle_length(i)
            if cycle_visited:
                max_cycle_length = max(max_cycle_length, depth)
        

        return max(max_cycle_length, free_component_total)