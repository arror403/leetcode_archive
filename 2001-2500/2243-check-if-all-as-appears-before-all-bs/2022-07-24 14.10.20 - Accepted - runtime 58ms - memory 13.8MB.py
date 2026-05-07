class Solution:
    def checkString(self, s: str) -> bool:
        s=list(s)
        return 1 if sorted(s)==s else 0