class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels=list(jewels)
        stones=list(stones)
        b=0
        
        for i in stones:
            if i in jewels:
                b+=1
                
        return b