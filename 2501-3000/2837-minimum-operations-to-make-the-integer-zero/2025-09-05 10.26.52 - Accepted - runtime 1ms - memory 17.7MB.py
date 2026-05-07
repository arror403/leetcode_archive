class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for n in range(61):
            t=num1-n*num2
            if t>=n and bin(t).count('1')<=n:
                return n

        return -1