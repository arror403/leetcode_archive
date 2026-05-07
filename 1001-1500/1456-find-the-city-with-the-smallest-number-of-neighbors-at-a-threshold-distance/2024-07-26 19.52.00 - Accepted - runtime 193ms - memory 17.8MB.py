class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def dijkstra(start):
            min_heap=[(0,start)]  # (distance, node)
            distances={i:inf for i in range(n)}
            distances[start]=0
            
            while min_heap:
                curr_dist,node=heapq.heappop(min_heap)
                
                if curr_dist>distances[node]: continue
                
                for neighbor,weight in graph[node]:
                    distance=curr_dist+weight
                    
                    if distance<distances[neighbor]:
                        distances[neighbor]=distance
                        heapq.heappush(min_heap, (distance, neighbor))

            return distances
            
        
        graph=defaultdict(list)

        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))
        
        min_neighbors=inf
        
        for city in range(n):
            distances=dijkstra(city)
            reachable=sum(1 for d in distances.values() if d<=distanceThreshold)
            
            if reachable<=min_neighbors:
                min_neighbors=reachable
                res=city
        

        return res