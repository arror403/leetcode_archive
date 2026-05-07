class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # Create adjacency list
        graph=[[] for _ in range(n+1)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # Initialize variables
        pq=[(0,1)]  # (time, node)
        visits=[[inf,inf] for _ in range(n+1)]
        visits[1][0]=0
        
        while pq:
            t,node=heapq.heappop(pq)
            # If we've reached the destination for the second time, return the time
            if node==n and t>visits[n][0]: return t
            # Calculate waiting time at traffic light
            if (x:=t//change)%2==1: t=(x+1)*change
            # Explore neighbors
            for x in graph[node]:
                new_time=t+time
                if new_time<visits[x][0]:
                    visits[x][1]=visits[x][0]
                    visits[x][0]=new_time
                    heapq.heappush(pq, (new_time,x))
                elif visits[x][0]<new_time<visits[x][1]:
                    visits[x][1]=new_time
                    heapq.heappush(pq, (new_time,x))

        # If no second minimum time found
        return -1  