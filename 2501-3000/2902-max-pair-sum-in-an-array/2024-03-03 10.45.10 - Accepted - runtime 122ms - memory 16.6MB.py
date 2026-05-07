class Solution:
    def maxSum(self, nums: List[int]) -> int:
        m=sorted([[v,max(list(map(int,str(v))))] for v in nums], key=lambda x:x[1])
        t=[list(g) for _,g in groupby(m, key=lambda x:x[1])]
        return max([sum(nlargest(2, [x[0] for x in i])) for i in t if len(i)>1], default=-1)