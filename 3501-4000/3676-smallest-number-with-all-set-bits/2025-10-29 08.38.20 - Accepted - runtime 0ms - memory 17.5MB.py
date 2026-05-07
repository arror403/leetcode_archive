class Solution:
    def smallestNumber(self, n: int) -> int:
        for x in [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]:
            if x >= n:
                return x