class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        res,cur=0,0

        for a,b in customers:
            cur=max(cur,a)
            
            finish_time=cur+b
            wait_time=finish_time-a

            res+=wait_time
            cur=finish_time

        return res/len(customers)