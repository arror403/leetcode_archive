class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        res=[]

        xor_all = 0
        # Calculate the XOR of all elements in nums
        for num in nums: xor_all ^= num

        # Calculate the maximum XOR for each query and remove the last element
        for i in range(len(nums)):
            k = 0
            for j in range(maximumBit-1, -1, -1):
                # Find the kth bit by checking if xor_all has a 0 or 1 at that position
                k_bit = (xor_all >> j) & 1
                k |= (1 - k_bit) << j

            res.append(k)
            xor_all ^= nums.pop()

        return res