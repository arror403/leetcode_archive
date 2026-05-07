class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        # Create adjacency list
        graph=[[] for _ in range(n)]
        for (a,b), p in zip(edges, succProb):
            graph[a].append((b, p))
            graph[b].append((a, p))
        
        probabilities = [0.0]*n
        probabilities[start] = 1.0
        
        # Priority queue for Dijkstra's algorithm
        pq=[(-1.0, start)]
        
        while pq:
            prob, node = heappop(pq)
            prob*=-1
            
            if node==end: return prob
            
            if prob<probabilities[node]: continue
            
            for neighbor,edge_prob in graph[node]:
                new_prob=prob*edge_prob
                if new_prob>probabilities[neighbor]:
                    probabilities[neighbor]=new_prob
                    heappush(pq, (-new_prob, neighbor))
        
        
        return 0.0