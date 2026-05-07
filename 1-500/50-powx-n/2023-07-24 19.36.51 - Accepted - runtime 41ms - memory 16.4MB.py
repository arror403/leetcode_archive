class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        if n < 0:
            x = 1 / x
            n = -n
        
        def power(x, n):
            if n == 0:
                return 1.0
            if n == 1:
                return x
            half_power = power(x, n // 2)
            if n % 2 == 0:
                return half_power * half_power
            else:
                return x * half_power * half_power
        
        return power(x, n)