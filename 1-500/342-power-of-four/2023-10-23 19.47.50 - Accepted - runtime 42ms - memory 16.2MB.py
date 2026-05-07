class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return False if n<=0 else (n&(n-1)==0) and (n&0xAAAAAAAA==0)