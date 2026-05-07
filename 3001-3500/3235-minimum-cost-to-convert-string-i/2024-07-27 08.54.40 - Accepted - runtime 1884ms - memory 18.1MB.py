class Solution:
    def minimumCost(self, source, target, original, changed, cost):
        dist=[[inf]*26 for _ in range(26)]
        for i in range(26): dist[i][i]=0

        # Build the initial graph
        for o,c,w in zip(original,changed,cost):
            i, j = ord(o)-ord('a'), ord(c)-ord('a')
            dist[i][j]=min(dist[i][j],w)

        # Floyd-Warshall algorithm
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dist[i][j]=min(dist[i][j], (dist[i][k]+dist[k][j]))

        # Calculate the minimum cost
        total_cost=0
        for s,t in zip(source,target):
            if s!=t:
                cost=dist[ord(s)-97][ord(t)-97]
                if cost==inf: return -1  # Impossible to convert
                total_cost+=cost


        return total_cost