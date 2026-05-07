class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        res=[]
 
        xor_all=reduce(lambda x,y: x^y, nums)

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
