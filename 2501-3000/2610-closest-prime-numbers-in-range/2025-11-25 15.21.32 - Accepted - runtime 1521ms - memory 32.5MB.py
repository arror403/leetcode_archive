class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = [True]*(right + 1)
        # 0 and 1 are non-prime
        sieve[0] = sieve[1] = False

        # Sieve of Eratosthenes: mark non-prime numbers
        p = 2
        while p*p <= right:
            if sieve[p]:
                # Mark multiples of p as non-prime
                for multiple in range(p*p, right + 1, p):
                    sieve[multiple] = False
            p += 1

        best_gap = inf
        best_pair = [-1, -1]
        previous_prime = -1

        for num in range(max(left, 2), right + 1):
            if sieve[num]:
                if previous_prime != -1:
                    gap = num - previous_prime
                    if gap < best_gap:
                        best_gap = gap
                        best_pair = [previous_prime, num]
                previous_prime = num


        return best_pair