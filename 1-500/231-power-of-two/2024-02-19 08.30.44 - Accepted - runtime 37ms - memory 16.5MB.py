class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return False if n<=0 else ceil(log2(n))==floor(log2(n))