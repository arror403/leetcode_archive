class Solution:
    def maxXorSubsequences(self, nums: List[int]) -> int:
        basis = [0] * 32
        res = 0
 
        for x in nums:
            while x:
                highestBitOn = 31 - len(bin(x)[2:])
                if basis[highestBitOn]:
                    x ^= basis[highestBitOn]
                else:
                    basis[highestBitOn] = x
                    break

        
        for i in basis: res = max(res, res ^ i)
        

        return res