class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        t=Counter(s)
        return '1'*(t['1']-1)+'0'*t['0']+'1'