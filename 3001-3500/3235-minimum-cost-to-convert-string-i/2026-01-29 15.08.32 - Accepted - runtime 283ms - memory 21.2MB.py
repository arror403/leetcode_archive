class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Build the graph: adjacency list where edges[src][dst] = weight
        # We use a nested dict to easily handle multiple edges by keeping the minimum cost
        edges = defaultdict(dict)
        for s, d, c in zip(original, changed, cost):
            edges[s][d] = min(edges[s].get(d, inf), c)
        # Function to find shortest paths from a specific start character (Dijkstra's Algorithm)
        def bfs_min_costs(start_node):
            min_costs = {start_node: 0}
            heap = [(0, start_node)]
            while heap:
                curr_cost, u = heappop(heap)
                # If we found a shorter path to u already, skip
                if curr_cost > min_costs[u]:
                    continue
                # Explore neighbors
                for v, w in edges[u].items():
                    new_cost = curr_cost + w
                    # If a cheaper path is found, update and push to heap
                    if new_cost < min_costs.get(v, inf):
                        min_costs[v] = new_cost
                        heappush(heap, (new_cost, v))
            return min_costs
        # Cache to store the shortest path results for every unique source character
        memo = {}
        total_cost = 0
        for s, t in zip(source, target):
            if s == t: continue
            # If we haven't calculated paths from 's' yet, run Dijkstra and cache it
            if s not in memo:
                memo[s] = bfs_min_costs(s)
            # Check if 't' is reachable from 's' using the cached results
            if t not in memo[s]:
                return -1
            total_cost += memo[s][t]

        return total_cost