class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return sum(c in "aeiou" for c in s)!=0