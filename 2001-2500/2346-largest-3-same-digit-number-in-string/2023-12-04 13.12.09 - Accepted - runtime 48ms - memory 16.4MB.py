class Solution:
    def largestGoodInteger(self, num: str) -> str:
        return max([k for k,g in groupby(num) if len(list(g))>=3],default="")*3