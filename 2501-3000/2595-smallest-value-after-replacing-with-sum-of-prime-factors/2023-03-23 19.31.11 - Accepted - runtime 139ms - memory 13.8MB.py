class Solution:
    def smallestValue(self, n: int) -> int:
        # print (self.prime_factors(n))
        
        while 1:
            if n==sum(self.prime_factors(n)):
                return n
            if self.is_prime(n): 
                return n
            else: 
                n=sum(self.prime_factors(n))


    def prime_factors(self, n):
        factors = []
        divisor = 2
        while divisor <= n:
            if n % divisor == 0:
                factors.append(divisor)
                n //= divisor
            else:
                divisor += 1
        return factors


    def is_prime(self, n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True