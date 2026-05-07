class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        L=len(baskets)
        res=0

        for f in fruits:
            c=True
            for i in range(L):
                if baskets[i]>=f:
                    baskets[i]=0
                    c=False
                    break
            if c: res+=1


        return res