class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        L=len(s)
        max_len=-1
        for i in range(L):
            for j in range(L-1, i, -1):
                if s[i]==s[j]:
                    max_len=max(max_len, j-i-1)
                    
        return max_len