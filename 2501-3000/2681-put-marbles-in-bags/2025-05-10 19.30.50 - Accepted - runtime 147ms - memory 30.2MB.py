class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n=len(weights)
        if (k==1 or n==k): return 0
        
        mins=maxs=0
        candidates=[a+b for a,b in pairwise(weights)]
        candidates.sort()

        for i in range(k-1):
            mins+=candidates[i]
            maxs+=candidates[n-2-i]


        return maxs-mins