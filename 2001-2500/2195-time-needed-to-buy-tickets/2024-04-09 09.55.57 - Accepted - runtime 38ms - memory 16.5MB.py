class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # tickets=deque(tickets)
        t=tickets[k]
        res=0

        while 1:
            for i in range(len(tickets)):
                if tickets[i]>0:
                    tickets[i]-=1
                    res+=1
                    if i==k: t-=1

                if t==0:
                    return res