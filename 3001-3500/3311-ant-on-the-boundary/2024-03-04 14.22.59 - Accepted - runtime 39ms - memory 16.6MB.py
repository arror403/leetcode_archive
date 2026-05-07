class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        p=0
        res=0
        for i in nums:
            p+=i
            if p==0:
                res+=1

        return res