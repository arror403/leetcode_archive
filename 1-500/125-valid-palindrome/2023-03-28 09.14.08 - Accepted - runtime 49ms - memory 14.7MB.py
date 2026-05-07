class Solution:
    def isPalindrome(self, s: str) -> bool:
        p,q="",""
        for i in range(len(s)):
            if s[i].isalnum():
                p+=s[i]
        q=p[::-1]
        return p.lower() == q.lower()