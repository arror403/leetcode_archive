class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        res=i=0
        j=len(costs)-1

        pq1=[]
        pq2=[]
        # priority_queue<int, vector<int>, greater<int>> pq1
        # priority_queue<int, vector<int>, greater<int>> pq2

        while k:
            while(len(pq1)<candidates and i<=j):
                heappush(pq1, costs[i])
                i+=1
            
            while(len(pq2)<candidates and i<=j):
                heappush(pq2, costs[j])
                j-=1

            t1=pq1[0] if pq1 else inf
            # t1 = pq1.size() > 0 ? pq1.top() : INT_MAX
            t2=pq2[0] if pq2 else inf
            # t2 = pq2.size() > 0 ? pq2.top() : INT_MAX

            if t1<=t2:
                res+=t1
                heappop(pq1)

            else:
                res+=t2
                heappop(pq2)

            k-=1


        return res