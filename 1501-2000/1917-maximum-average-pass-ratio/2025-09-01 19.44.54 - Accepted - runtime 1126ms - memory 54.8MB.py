class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        def profit(p, t): return -((p+1)/(t+1)-p/t)
        
        total=0
        pq=[]

        for c in classes:
            total+=c[0]/c[1]
            heappush(pq, (profit(c[0], c[1]), c[0], c[1]))
        
        for _ in range(extraStudents):
            np, p, t = heappop(pq)
            total -= np
            heappush(pq, (profit(p+1, t+1), p+1, t+1))


        return total/len(classes)