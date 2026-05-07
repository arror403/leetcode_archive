class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        if n==1: return m if k==0 else 0
        MOD = 10**9+7
        def modExp(base, exp):
            result = 1
            while (exp > 0):
                if ((exp & 1) == 1):
                    result = (result * base) % MOD
                
                base = (base**2) % MOD
                exp //= 2

            return result
        

        return ((comb(n-1, k) * m) * modExp(m-1, n-k-1)) % MOD