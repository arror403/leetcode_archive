class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # Generate primes up to 1000 using sieve
        primes = []
        sieve = [True] * 1001
        for i in range(2, int(1001 ** 0.5) + 1):
            if sieve[i]:
                primes.append(i)
                for j in range(i * i, 1001, i):
                    sieve[j] = False
        primes.extend([i for i in range(int(1001 ** 0.5) + 1, 1001) if sieve[i]])
        
        prev = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < prev:
                prev = nums[i]
                continue
            
            # Find largest prime that works
            found = False
            for prime in primes:
                if prime >= nums[i]:
                    break
                if nums[i] - prime < prev:
                    prev = nums[i] - prime
                    found = True
                    break
            if not found:
                return False
                
        return True