class Solution:
    def minOperations(self, s: str) -> int:
        return 0 if set(s)=={'a'} else 123-min(ord(c) for c in (set(s)-{'a'}))