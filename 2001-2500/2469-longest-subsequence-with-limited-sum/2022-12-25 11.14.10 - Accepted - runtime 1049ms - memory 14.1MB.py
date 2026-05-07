class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        res=[]
        for i in queries:
            s,t=0,0
            for j in nums:
                if (s+j)<=i:
                    s+=j
                    # print(nums[j])
                    t+=1
            res.append(t)
        return res