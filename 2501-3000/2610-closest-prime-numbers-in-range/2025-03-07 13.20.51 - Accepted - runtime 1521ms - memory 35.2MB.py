class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve=[True]*(right+1)
        sieve[0]=sieve[1]=False
        
        i=2
        while i**2<=right:
            if sieve[i]:
                for j in range(i**2, right+1, i):
                    sieve[j]=False
            i+=1

        primes=[]
        for i in range(left, right+1):
            if sieve[i]:
                primes.append(i)
        
        if len(primes)<2: return [-1,-1]
        
        min_gap=inf
        res=[-1,-1]
        
        for a,b in pairwise(primes):
            gap=b-a
            if gap<min_gap:
                min_gap=gap
                res=[a,b]
        

        return res