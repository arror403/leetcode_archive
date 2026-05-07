class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        return sum(sum(1 for _ in set(s[s.index(c)+1:s.rindex(c)])) for c in set(s) if s.count(c)>1)