class Solution:
    def countSubstrings(self, s: str) -> int:

        @lru_cache(maxsize=None)
        def isPalindrome(i,j):
            return True if (i>=j) else (s[i]==s[j] and isPalindrome(i+1,j-1))

        res=0
        L=len(s)

        for i in range(L):
            for j in range(i,L):
                if isPalindrome(i,j):
                    res+=1

        return res