class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n < 2: return 1
        
        component_count = 0
        G = defaultdict(list)
        in_degree = [0]*n

        # Build the graph and calculate in-degrees
        for n1, n2 in edges:
            G[n1].append(n2)
            G[n2].append(n1)
            in_degree[n1] += 1
            in_degree[n2] += 1

        # Initialize the queue with nodes having in-degree of 1 (leaf nodes)
        q = deque(node for node in range(n) if in_degree[node] == 1)

        while q:
            current_node = q.popleft()
            in_degree[current_node] -= 1
            add_value = 0

            # Check if the current node's value is divisible by k
            if values[current_node] % k == 0:
                component_count += 1
            else:
                add_value = values[current_node]

            # Propagate the value to the neighbor nodes
            for neighbor_node in G[current_node]:
                if in_degree[neighbor_node] == 0:
                    continue
                in_degree[neighbor_node] -= 1
                values[neighbor_node] += add_value

                # If the neighbor node's in-degree becomes 1, add it to the queue
                if in_degree[neighbor_node] == 1:
                    q.append(neighbor_node)


        return component_count