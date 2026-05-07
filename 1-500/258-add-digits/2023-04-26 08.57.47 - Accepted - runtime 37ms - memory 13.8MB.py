class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            num=list(map(int,str(num)))
            num=sum(num)
        return num