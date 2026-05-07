class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # Try all possible values of p and q
        for p in range(1, n-1):
            for q in range(p+1, n-1):
                # Check if nums[0...p] is strictly increasing
                is_first_increasing = True
                for i in range(p):
                    if nums[i] >= nums[i+1]:
                        is_first_increasing = False
                        break
                
                if not is_first_increasing:
                    continue
                
                # Check if nums[p...q] is strictly decreasing
                is_middle_decreasing = True
                for i in range(p, q):
                    if nums[i] <= nums[i+1]:
                        is_middle_decreasing = False
                        break
                
                if not is_middle_decreasing:
                    continue
                
                # Check if nums[q...n-1] is strictly increasing
                is_last_increasing = True
                for i in range(q, n-1):
                    if nums[i] >= nums[i+1]:
                        is_last_increasing = False
                        break
                
                if is_last_increasing:
                    return True
        
        return False