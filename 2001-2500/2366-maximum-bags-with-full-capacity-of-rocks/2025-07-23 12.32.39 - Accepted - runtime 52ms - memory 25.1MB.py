class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        t=[b-a for a,b in zip(rocks, capacity)]
        t.sort()
        
        res=0
        for x in t:
            if additionalRocks>=x:
                additionalRocks-=x
                res+=1
                if additionalRocks<=0: break
                

        return res