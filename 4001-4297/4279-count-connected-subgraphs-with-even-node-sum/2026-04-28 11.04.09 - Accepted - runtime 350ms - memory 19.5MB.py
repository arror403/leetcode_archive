class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        p = [[0] * n for _ in range(n)]
        for u, v in edges:
            p[u][v] = 1
            p[v][u] = 1 # undirected

        def is_connected(subset: tuple[int]) -> bool:
            if not subset: return False
            
            start_node = subset[0]
            queue = deque([start_node])
            visited = {start_node}
            subset_set = set(subset) # Quick lookup for subset membership
            
            while queue:
                u = queue.popleft()
                # Check all potential neighbors (0 to n-1)
                for v in range(n):
                    # 1. Is there an edge between u and v? (p[u][v] == 1)
                    # 2. Is v part of the current subset? (v in subset_set)
                    # 3. Have we not visited v yet? (v not in visited)
                    if p[u][v] == 1 and v in subset_set and v not in visited:
                        visited.add(v)
                        queue.append(v)
            # If the count of visited nodes equals the size of the subset, it is connected.
            return len(visited) == len(subset)

        res = 0
        for r in range(1, n + 1):
            for t in combinations(range(n), r):
                if sum(nums[i] for i in t) % 2 != 0:
                    continue
                if is_connected(t):
                    res += 1

        return res