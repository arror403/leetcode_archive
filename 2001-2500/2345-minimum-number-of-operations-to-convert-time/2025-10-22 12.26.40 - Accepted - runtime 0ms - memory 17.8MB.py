class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        d = (int(correct[:2]) * 60 + int(correct[-2:])) - (int(current[:2]) * 60 + int(current[-2:]))
        op = 0

        if d >= 60:
            op += (d//60)
            d %= 60
        if d >= 15:
            op += (d//15)
            d %= 15
        if d >= 5:
            op += (d//5)
            d %= 5


        return op + d