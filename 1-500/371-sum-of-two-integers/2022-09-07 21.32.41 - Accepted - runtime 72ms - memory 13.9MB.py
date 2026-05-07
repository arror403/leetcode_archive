class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a==0: return b
        elif b==0: return a
        else: return int(math.log(math.exp(a)*math.exp(b)))