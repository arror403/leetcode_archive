class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        return f"{'1'*(Counter(s)['1']-1)}{'0'*Counter(s)['0']}1"