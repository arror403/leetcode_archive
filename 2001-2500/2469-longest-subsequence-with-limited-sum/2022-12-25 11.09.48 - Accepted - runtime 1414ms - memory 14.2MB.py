class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        res=[]
        for i in queries:
            s,t=0,0
            for j in range(len(nums)):
                if (s+nums[j])<=i:
                    s+=nums[j]
                    # print(nums[j])
                    t+=1
            res.append(t)
        return res