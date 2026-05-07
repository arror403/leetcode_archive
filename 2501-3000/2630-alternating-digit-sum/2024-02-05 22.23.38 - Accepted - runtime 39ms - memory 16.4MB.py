class Solution:
    def alternateDigitSum(self, n: int) -> int:
        return sum(int(x) for x in str(n)[::2])-sum(int(x) for x in str(n)[1::2])