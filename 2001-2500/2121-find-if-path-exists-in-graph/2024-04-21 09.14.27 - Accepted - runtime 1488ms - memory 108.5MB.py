class Solution:
    ##### helped by Claude #####
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        def BFS(graph, start, end):
            queue = deque([(start, [start])])
            visited = set()

            while queue:
                node, path = queue.popleft()
                if node == end:
                    return path

                if node not in visited:
                    visited.add(node)
                    for neighbor in graph[node]:
                        queue.append((neighbor, path + [neighbor]))

            return None  # no path found


        def build_graph(edges, n):
            graph = {node: [] for node in range(n)}
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph


        graph=build_graph(edges, n)
        path = BFS(graph, source, destination)

        return 1 if path else 0