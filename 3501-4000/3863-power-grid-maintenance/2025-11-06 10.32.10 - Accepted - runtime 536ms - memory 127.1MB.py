class Solution:
    def processQueries(self, c, connections, queries) -> List[int]:
        # Step 1: Build the adjacency list representation of the graph.
        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        # Step 2: Find all connected components using Depth First Search (DFS).
        ids = {}  
        components = defaultdict(list)
        visited = [False] * (c + 1) # 1 indexed, visited[0] won't be used
        def dfs(node, component_id):
            visited[node] = True
            ids[node] = component_id
            components[component_id].append(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor, component_id)

        # Iterate through all nodes to find all components.
        for i in range(1, c + 1):
            if not visited[i]:
                # We found a new, unvisited component.
                # Use the first node `i` we find as the ID for this component.
                dfs(i, i)
                # Sort the nodes in the component to easily find the smallest later.
                components[i].sort()

        # --- OPTIMIZATION ---
        # This dictionary will store the index of the smallest available node for each component.
        component_min_idx = defaultdict(int)
        # This set stores all nodes that have been "removed" by type 2 queries.
        removed = set()
        result = []

        # Step 3: Process queries efficiently.
        for q_type, node in queries:
            if q_type == 1:  # "Find" query
                component_id = ids.get(node)
                # Case 1: The queried node itself is available. This is the best-case answer.
                if node not in removed:
                    result.append(node)
                    continue
                # Case 2: The queried node was removed. Find the smallest available in its component.
                # If a node doesn't exist in any connection, it won't be in `ids`.
                if component_id is None:
                    result.append(-1)
                    continue
                    
                # Get the current pointer for this component.
                current_idx = component_min_idx[component_id]
                nodes_in_comp = components[component_id]
                
                # Advance the pointer past any nodes that have been removed.
                while current_idx < len(nodes_in_comp) and nodes_in_comp[current_idx] in removed:
                    current_idx += 1
                
                # Update the pointer for this component for future queries.
                component_min_idx[component_id] = current_idx
                
                if current_idx < len(nodes_in_comp):
                    # We found the smallest available node.
                    result.append(nodes_in_comp[current_idx])
                else:
                    # All nodes in this component have been removed.
                    result.append(-1)
            
            else: # q_type == 2
                removed.add(node)
        

        return result