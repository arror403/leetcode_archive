class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        even_count = (n + 1) // 2
        odd_count = n // 2
        
        def mod_pow(base, exp, mod):
            result = 1
            base %= mod

            while exp > 0:
                # If exp is odd
                if exp & 1: result = (result * base) % mod

                # Divide exp by 2
                exp >>= 1
                base = (base * base) % mod

            return result
        

        return (mod_pow(5, even_count, MOD) * mod_pow(4, odd_count, MOD)) % MOD