class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        # d=Counter([(24-v)%24 for v in hours])
        # p=[[a,b] for a,b in combinations(d.keys(),2) if (a+b)==24]
        # return sum(d[a]*d[b] for a,b in p)

        remainder_count=[0]*24
        res=0
        for v in hours: remainder_count[v%24]+=1
                
        # Count pairs for remainder 0
        res+=(remainder_count[0]*(remainder_count[0]-1))//2
        # Count pairs for remainder 12
        res+=(remainder_count[12]*(remainder_count[12]-1))//2
        # Count pairs for other remainders
        for r in range(1,12): res+=remainder_count[r]*remainder_count[24 - r]


        return res