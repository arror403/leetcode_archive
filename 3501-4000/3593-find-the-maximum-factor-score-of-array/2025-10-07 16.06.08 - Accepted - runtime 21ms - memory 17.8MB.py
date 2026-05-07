class Solution:
    def maxScore(self, nums: List[int]) -> int:
        m=set(nums)
        if len(m)==1: return nums[0]**2
        d=Counter(nums)


        def L(numbers): return reduce(lambda x,y: x*y//gcd(x,y), numbers, 1)

        def G(numbers): return reduce(lambda x,y: gcd(x,y), numbers)

        res=L(list(m))*G(list(m))

        for x in m:
            if d[x]>1: continue
            tmp=list(m-{x})
            res=max(res, L(tmp)*G(tmp))


        return res

        # d={1: {1}, 2: {1, 2}, 3: {1, 3}, 4: {1, 2, 4}, 5: {1, 5}, 6: {1, 2, 3, 6}, 7: {1, 7}, 8: {8, 1, 2, 4}, 9: {1, 3, 9}, 10: {1, 10, 2, 5}, 11: {1, 11}, 12: {1, 2, 3, 4, 6, 12}, 13: {1, 13}, 14: {1, 2, 14, 7}, 15: {1, 3, 5, 15}, 16: {1, 2, 4, 8, 16}, 17: {1, 17}, 18: {1, 2, 3, 6, 9, 18}, 19: {1, 19}, 20: {1, 2, 4, 5, 10, 20}, 21: {1, 3, 21, 7}, 22: {1, 2, 11, 22}, 23: {1, 23}, 24: {1, 2, 3, 4, 6, 8, 12, 24}, 25: {1, 5, 25}, 26: {1, 26, 2, 13}, 27: {3, 1, 27, 9}, 28: {1, 2, 4, 7, 14, 28}, 29: {1, 29}, 30: {1, 2, 3, 5, 6, 10, 15, 30}}