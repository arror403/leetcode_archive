class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        max_xor = (1 << maximumBit) - 1
        xor_all = reduce(lambda x,y:x^y , nums)
        res = [0] * n

        # for i in range(n):
        #     xor_all ^= nums[i]

        for i in range(n):
            res[i] = max_xor ^ xor_all
            xor_all ^= nums.pop()

        return res