class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # 1. Build Adjacency List
        # Using a dict of lists is more memory efficient than an N*N matrix
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w*2)) 

        # 2. Dijkstra's Algorithm Initialization
        # Min-heap stores: (current_total_cost, current_node)
        pq = [(0,0)] 
        
        # Track the minimum cost to reach every node found so far
        costs = [inf] * n
        costs[0] = 0

        while pq:
            # Pop the node with the smallest cost currently in the queue
            curr_cost, u = heappop(pq)

            # If we reached the destination, this is guaranteed to be the min cost
            if u == n - 1:
                return curr_cost

            # Optimization: If we found a path to 'u' that is worse than 
            # one we already processed, skip it.
            if curr_cost > costs[u]:
                continue

            # Check neighbors
            for v, w in graph[u]:
                new_cost = curr_cost + w
                
                # If we found a shorter path to neighbor v, update it and push to heap
                if new_cost < costs[v]:
                    costs[v] = new_cost
                    heappush(pq, (new_cost, v))

        # If we exhaust the queue and never reach n-1
        return -1