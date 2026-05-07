class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        L = len(nums[0])
        
        for i in range(1<<L):
            t = bin(i)[2:].zfill(L)

            if t not in nums:
                return t