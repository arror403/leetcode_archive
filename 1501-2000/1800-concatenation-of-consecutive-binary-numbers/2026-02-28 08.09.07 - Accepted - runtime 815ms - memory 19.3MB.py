class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = 0 
        MOD = (10**9 + 7)
        
        for i in range(1, n+1):
            L = int(log2(i))+1
            res = ((res << L) % MOD + i) % MOD


        return res