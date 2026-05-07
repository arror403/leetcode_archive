class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for n in range(61):
            t=num1-n*num2
            # if bin(num1-n*num2).count('1')==n:
            if t>=0 and bin(t).count('1') <= n <= t:
                return n

        return -1