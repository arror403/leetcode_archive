class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Calculate the maximum possible OR value first
        target=0
        for n in nums: target|=n
        
        def backtrack(pos, curr_or):
            if pos==len(nums): return curr_or==target
            # Take current number
            count = backtrack(pos + 1, curr_or | nums[pos])
            # Don't take current number
            count += backtrack(pos + 1, curr_or)
            
            return count


        return backtrack(0,0)