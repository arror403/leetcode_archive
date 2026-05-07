class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        # Check if it's a power of two (only one bit set) and if the bit is at an even position (0-based).
        if (n & (n - 1) == 0) and (n & 0xAAAAAAAA == 0):
            return True

        return False