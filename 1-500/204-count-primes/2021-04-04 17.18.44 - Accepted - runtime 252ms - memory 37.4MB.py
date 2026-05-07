class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)

        
        
        
        
        
#         if n==0&n==1: return 0
#         elif(n==2): return 1
#         else:
#             sum=1
#             for i in range(3,n,2):
#                 if (self.isPrime(i)): sum+=1 


#             return sum
        
        
        
#     def isPrime(self, n: int) -> bool:
#         if (n<=1) : return 0
#         if (n<=3) : return 1
#         if (n%2==0 or n%3==0): return 0
#         i=5
#         while(i*i<=n):
#             if (n%i==0 or n%(i+2)==0):
#                 return 0
#             i=i+6
#         return 1