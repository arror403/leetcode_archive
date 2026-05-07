class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0

        for x in range(97, 124):
            c = chr(x)
            i, j = s.find(c), s.rfind(c)
            if i >= 0:
                res += len(set(s[i+1:j]))
        
        
        return res