class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True]*n

        for i in range(2, int(sqrt(n))+1):
            if isPrime[i]:
                for j in range(i**2, n, i):
                    isPrime[j] = False


        return len([1 for p in isPrime[2:] if p])