class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res=inf
        nums=list(permutations([i for i in range(1,len(pattern)+2)]))

        for m in nums:
            if all((x=='I' and p[0]<p[1]) or (x=='D' and p[0]>p[1]) for x,p in zip(pattern, pairwise(m))):
                res=min(res, int(''.join([str(i) for i in m])))


        return str(res)