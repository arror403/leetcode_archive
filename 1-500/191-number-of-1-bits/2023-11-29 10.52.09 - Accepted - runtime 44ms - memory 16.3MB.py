class Solution:
    def hammingWeight(self, n: int) -> int:

        ##### power by chatGPT #####

        count = 0
        while n:
            # Increment count if the least significant bit is 1
            count += n & 1
            # Right shift n to check the next bit
            n >>= 1
        return count