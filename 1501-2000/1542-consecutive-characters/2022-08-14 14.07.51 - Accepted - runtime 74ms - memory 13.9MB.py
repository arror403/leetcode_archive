class Solution:
    def maxPower(self, s: str) -> int:
        # print(sorted([list(y) for x,y in groupby(list(s))],key=len))
        return len(sorted([list(y) for x,y in groupby(list(s))],key=len)[-1])