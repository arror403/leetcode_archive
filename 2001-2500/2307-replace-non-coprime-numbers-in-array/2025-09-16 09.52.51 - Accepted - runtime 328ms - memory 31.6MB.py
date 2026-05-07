class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def primeFactors(n):
            factors = set()
            while n % 2 == 0:
                factors.add(2)
                n //= 2
            for i in range(3, int(sqrt(n)) + 1, 2):
                while n % i == 0:
                    factors.add(i)
                    n //= i
            if n > 1: factors.add(n)
            return factors
        
        factor_cache = {}
        result = []
        
        for num in nums:
            result.append(num)
            
            while len(result) > 1:
                if result[-1] not in factor_cache:
                    factor_cache[result[-1]] = primeFactors(result[-1])
                if result[-2] not in factor_cache:
                    factor_cache[result[-2]] = primeFactors(result[-2])
                
                if factor_cache[result[-1]] & factor_cache[result[-2]]:
                    a, b = result.pop(), result.pop()
                    merged = lcm(a, b)
                    result.append(merged)
                else:
                    break
                    
        return result