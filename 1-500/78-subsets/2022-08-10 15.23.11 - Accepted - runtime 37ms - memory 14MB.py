class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        for i in range(len(nums)+1):
            tmp=itertools.combinations(nums,i)
            for j in tmp: res.append(j)
        return res
            