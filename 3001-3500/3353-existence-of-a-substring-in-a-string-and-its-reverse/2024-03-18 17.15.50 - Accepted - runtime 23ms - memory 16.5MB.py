class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        return next((1 for i in range(len(s)-1) if s[i:i+2] in s[::-1]), 0)