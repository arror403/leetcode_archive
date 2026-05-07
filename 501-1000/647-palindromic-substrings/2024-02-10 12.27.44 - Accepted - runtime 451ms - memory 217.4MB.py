class Solution:
    def countSubstrings(self, s: str) -> int:
        return len([i for i in [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)] if i==i[::-1]])