class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        ##### power by chatGPT #####
        return n>0 and (n&(n-1))==0