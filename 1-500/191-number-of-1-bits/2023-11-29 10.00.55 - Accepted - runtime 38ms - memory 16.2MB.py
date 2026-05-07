class Solution:
    def hammingWeight(self, n: int) -> int:
        # print(n,str(n))
        return bin(n).count("1")