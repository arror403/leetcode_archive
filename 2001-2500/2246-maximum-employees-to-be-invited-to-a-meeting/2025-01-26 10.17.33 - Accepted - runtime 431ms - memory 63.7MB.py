class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        """
        Solve the maximum invitations problem using graph traversal.
        
        Args:
            favorite (List[int]): List where favorite[i] is the favorite person of person i.
        
        Returns:
            int: Maximum number of people that can be invited to a party.
        """
        n = len(favorite)
        
        # Initialize tracking arrays
        depths = [-1] * n  # Tracks node depths
        reverse_graph = [[] for _ in range(n)]  # Reverse adjacency list
        
        # Build reverse graph
        for i, v in enumerate(favorite):
            reverse_graph[v].append(i)
        
        # Free component (mutual favorite pair) tracking
        free_component_total = 0
        
        def dfs_arm_length(node):
            """
            Depth-first search to find the longest arm length.
            
            Args:
                node (int): Starting node to explore.
            
            Returns:
                int: Length of the longest arm.
            """
            if depths[node] != -1:
                return depths[node]
            
            max_depth = 0
            for neighbor in reverse_graph[node]:
                max_depth = max(max_depth, dfs_arm_length(neighbor))
            
            depths[node] = 1 + max_depth
            return depths[node]
        
        # Handle mutual favorite pairs (free components)
        for i in range(n):
            if depths[i] != -1:
                continue
            
            if favorite[favorite[i]] == i:
                depths[i] = depths[favorite[i]] = 0
                
                # Find longest arms from both nodes
                arm1_length = max(
                    (dfs_arm_length(v) for v in reverse_graph[i] if v != favorite[i]), default=0)
                
                arm2_length = max(
                    (dfs_arm_length(v) for v in reverse_graph[favorite[i]] if v != i), default=0)
                
                free_component_total += arm1_length + arm2_length + 2
        
        def dfs_cycle_length(node):
            """
            Depth-first search to find cycle length.
            
            Args:
                node (int): Starting node to explore.
            
            Returns:
                tuple: (entry point, max depth, is cycle complete)
            """
            if depths[node] != -1:
                return (node, depths[node], False)
            
            depths[node] = 0
            entry_point, depth, cycle_visited = dfs_cycle_length(favorite[node])
            
            if cycle_visited:
                return (entry_point, depth, True)
            
            depths[node] = 1 + depth
            return (entry_point, depths[node], node == entry_point)
        
        # Find maximum cycle length
        max_cycle_length = 0
        for i in range(n):
            if depths[i] != -1:
                continue
            
            _, depth, cycle_visited = dfs_cycle_length(i)
            if cycle_visited:
                max_cycle_length = max(max_cycle_length, depth)
        

        return max(max_cycle_length, free_component_total)



        # sys.setrecursionlimit(10**9)
        # N=len(favorite)
        # res=free=0
        # m=[-1]*N
        # r=[m for _ in range(N)]
        # for i,v in enumerate(favorite): r[v].append(i)
        # #vector<int> m(N, -1); 
        # #// m[i] is the depth of node i. -1 means unvisited
        # #vector<vector<int>> r(N); 
        # #// The reverse graph
        # # for (int i = 0; i < N; ++i) r[A[i]].push_back(i);
        # #// handle case 1

        # # function<int(int)> dfs = [&](int u)
        # def dfs(u):
        #     if m[u]!=-1: return m[u]
        #     res=0
        #     for v in r[u]: res=max(res,dfs(v))
        #     m[u]=1+res
        #     return m[u]

        # for i in range(N):
        #     if m[i]!=-1: continue
        #     #// skip visited nodes
        #     if favorite[favorite[i]]==i:
        #         m[i] = m[favorite[i]] = 0
        #         a = b = 0
        #         #// find the length of the longest arms starting from `i` and `A[i]`
        #         for v in r[i]:
        #             if v==favorite[i]: continue
        #             a = max(a, dfs(v))
                
        #         for v in r[favorite[i]]: 
        #             if v==i: continue
        #             b = max(b, dfs(v))
                
        #         free+=(a+b+2)
        #         #// this free component is of length `a+b+2`

        # #// handle case 2
        # def dfs2(u):
        # # function<tuple<int, int, bool>(int)> dfs2 = [&](int u)->tuple<int, int, bool>
        #     if m[u]!=-1: return [u, m[u], False]
        #     #// We visited this node the second time, so this node must be the entry point to the cycle
        #     m[u]=0
        #     entryPoint, depth, cycleVisited = dfs2(favorite[u])
        #     if cycleVisited:
        #         #// After the cycle being traversed, any other node in the backtracking process are outside of the cycle and should be ignored (by keeping m[u] as 0).
        #         return [entryPoint, depth, True]

        #     m[u]=1+depth
        #     #// If we haven't met the entry point again, this is a node within the cycle, so we increment the depth.
        #     return [entryPoint, m[u], u==entryPoint]
        #     #// When we visit the entry point again, we know what we've done traversing the cycle.

        # for i in range(N):
        #     if m[i]!=-1: continue
        #     entryPoint, depth, cycleVisited = dfs2(i)
        #     if cycleVisited: res = max(res, depth)


        # return max(res, free)