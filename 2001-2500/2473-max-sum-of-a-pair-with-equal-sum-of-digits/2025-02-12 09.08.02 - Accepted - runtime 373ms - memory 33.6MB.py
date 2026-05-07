class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        d=defaultdict(list)
        res=-1

        for v in nums:
            digit_sum=sum(map(int,str(v)))
            d[digit_sum].append(v)

        for t in d.values():
            if len(t)>=2:
                res=max(res, t[0]+t[1])


        return res