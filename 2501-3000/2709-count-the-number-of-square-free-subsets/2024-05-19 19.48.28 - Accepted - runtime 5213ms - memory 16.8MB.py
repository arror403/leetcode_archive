class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD=10**9+7
        res=-1
        d=Counter(nums)
        m=set([1, 2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30])
        p = {
            1: [1], 2: [2], 3: [3], 5: [5], 6: [2, 3], 7: [7], 10: [2, 5], 11: [11],
            13: [13], 14: [2, 7], 15: [3, 5], 17: [17], 19: [19], 21: [3, 7], 22: [2, 11],
            23: [23], 26: [2, 13], 29: [29], 30: [2, 3, 5]
        }
        s=d.keys()&m

        powerset=chain.from_iterable(combinations(s,r) for r in range(len(s)+1))

        for x in powerset:
            tmp=[]
            for i in x: tmp+=p[i]

            if len(tmp)==len(set(tmp)):
                if 1 in tmp:
                    res+=prod([d[v] for v in x if v!=1])*(2**d[1]-1)
                    res%=MOD
                elif tmp==[1]:
                    res+=2**d[1]-1
                    res%=MOD
                else:
                    res+=prod([d[v] for v in x])
                    res%=MOD


        return res