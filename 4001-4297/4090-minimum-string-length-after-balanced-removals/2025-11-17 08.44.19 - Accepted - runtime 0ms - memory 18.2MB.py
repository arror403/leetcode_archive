class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        return abs(len(s)-s.count('a')*2)