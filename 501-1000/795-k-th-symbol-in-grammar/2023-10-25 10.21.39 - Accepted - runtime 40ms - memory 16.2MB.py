class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        res = 0
        while (k>1):
            if k%2==1: k+=1
            else: k//=2
            res ^= 1
        
        return res