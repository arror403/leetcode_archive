class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        return -1 if x%(w:=sum(map(int,str(x))))!=0 else w