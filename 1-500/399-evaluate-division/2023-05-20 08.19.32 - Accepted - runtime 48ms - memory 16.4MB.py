class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Step 1: Build the graph
        graph = {}
        for (dividend, divisor), value in zip(equations, values):
            if dividend in graph:
                graph[dividend].append((divisor, value))
            else:
                graph[dividend] = [(divisor, value)]
            if divisor in graph:
                graph[divisor].append((dividend, 1 / value))
            else:
                graph[divisor] = [(dividend, 1 / value)]

        # Step 2: Perform DFS on each query
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            for neighbor, value in graph[start]:
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return value * result
            return -1.0

        # Step 3: Evaluate each query
        results = []
        for query in queries:
            dividend, divisor = query
            visited = set()
            result = dfs(dividend, divisor, visited)
            results.append(result)

        return results