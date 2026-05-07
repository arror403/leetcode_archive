class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res=[]
        self.tmp=[]
        nums.sort()

        def backtrack(remain, start):
            if remain<0:
                return
            elif remain==0:
                self.res.append(self.tmp[:])
            else:
                for i in range(start,len(nums)):
                    self.tmp.append(nums[i])
                    backtrack(remain-nums[i], i)
                    self.tmp.pop()


        backtrack(target, 0)


        return self.res