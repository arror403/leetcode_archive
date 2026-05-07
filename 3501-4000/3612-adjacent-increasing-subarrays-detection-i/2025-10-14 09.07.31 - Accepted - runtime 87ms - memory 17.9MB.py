class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums) - 2*k+1):
            a = nums[i:i+k]
            b = nums[i+k:i+2*k]
            # print(a,b)
            if a == sorted(a) and b == sorted(b):
                if len(set(a)) == len(set(b)) == k:
                    return True
            

        return False