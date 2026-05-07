class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        # m=[(bin(v)[2:]).zfill(16) for v in nums]
        return len(nums)%2==0 or reduce(operator.xor, nums)==0