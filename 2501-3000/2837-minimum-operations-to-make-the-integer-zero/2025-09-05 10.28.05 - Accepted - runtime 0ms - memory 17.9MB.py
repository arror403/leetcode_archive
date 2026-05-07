class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for n in range(61):
            t=num1-n*num2
            if t>=n and t.bit_count()<=n:
                return n

        return -1