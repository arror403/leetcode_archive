class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(maxsize=None)
        def lps(i, j):
            # Base case: if the substring is empty or a single character
            if i>j:  return 0
            if i==j: return 1
            
            # If the characters at the current positions are the same
            if s[i]==s[j]: return 2+lps(i+1, j-1)
            
            # If the characters are different, take the maximum of ignoring one character
            return max(lps(i+1, j), lps(i, j-1))
        
        return lps(0, len(s)-1)