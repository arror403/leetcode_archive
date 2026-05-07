class Solution:
    def maxScore(self, speed: List[int], efficiency: List[int], k: int) -> int:
        n=len(speed)
        total=res=0
        pq=[]

        ess=sorted(zip(speed, efficiency), key=lambda x: -x[1])

        for s,e in ess:
            heappush(pq, s)
            total+=s
            if len(pq)>k: total-=heappop(pq)
            
            if len(pq)==k: res=max(res, total*e)
        

        return res