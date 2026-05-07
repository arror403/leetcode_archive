class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        b=0
        for i in range(0,len(jewels)):
            for j in range(0,len(stones)):
                if jewels[i]==stones[j]:
                    b+=1
        
        return b