class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist=[[inf]*n for _ in range(n)]
        min_neighbors=inf
        result_city=-1

        for i in range(n): dist[i][i]=0
        
        for a,b,w in edges:
            dist[a][b]=w
            dist[b][a]=w
        
        # Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j]=min(dist[i][j], (dist[i][k]+dist[k][j]))
        # print(dist)
        
        # Count reachable cities for each city
        for city in range(n):
            reachable=sum(1 for neighbor in range(n) if dist[city][neighbor]<=distanceThreshold)
            
            # Update result if this city has fewer or equal reachable neighbors
            if reachable<=min_neighbors:
                min_neighbors=reachable
                res=city
        

        return res