class Solution:
    def alternateDigitSum(self, n: int) -> int:
        return sum(int(v) if i%2==0 else -int(v) for i,v in enumerate(str(n)))