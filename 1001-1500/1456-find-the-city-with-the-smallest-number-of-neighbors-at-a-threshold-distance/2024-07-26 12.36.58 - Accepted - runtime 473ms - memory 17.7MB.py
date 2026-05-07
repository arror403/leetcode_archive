class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Initialize distance matrix with infinity
        dist=[[inf]*n for _ in range(n)]
        # Set distance to self as 0
        for i in range(n): dist[i][i]=0
        
        # Fill in the known distances from edges
        for from_city, to_city, weight in edges:
            dist[from_city][to_city] = weight
            dist[to_city][from_city] = weight
        
        # Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        min_neighbors = inf
        result_city = -1
        
        # Count reachable cities for each city
        for city in range(n):
            reachable = sum(1 for neighbor in range(n) if dist[city][neighbor]<=distanceThreshold)
            
            # Update result if this city has fewer or equal reachable neighbors
            if reachable<=min_neighbors:
                min_neighbors = reachable
                result_city = city
        
        
        return result_city