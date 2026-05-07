class Solution:
    def doesAliceWin(self, s: str) -> bool:
        t=sum(1 if c in "aeiou" else 0 for c in s)

        return False if t==0 else True