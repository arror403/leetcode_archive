class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        f=times[targetFriend][0]
        times.sort(key=lambda x:x[0])
        n=0
        q=[]
        s=[]
        
        for a,b in times:
            while q and q[0][0]<=a:
                heappush(s, heappop(q)[1])

            if s:
                cs=heappop(s)
            else:
                cs=n
                n+=1

            heappush(q, (b,cs))

            if f==a: return cs


        return 0