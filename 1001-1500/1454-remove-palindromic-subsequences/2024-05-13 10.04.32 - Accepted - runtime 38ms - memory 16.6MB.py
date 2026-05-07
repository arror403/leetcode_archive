class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 2 if s!=s[::-1] else 1