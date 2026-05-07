class Solution:
    def isPalindrome(self, s: str) -> bool:
        p=""
        q=""
        for i in range(len(s)):
            if s[i].isalnum():
                p+=s[i]
                
        for i in range(len(p)-1,-1,-1):
            q+=p[i]
        
        if p.lower() == q.lower():
            return 1
        else:
            return 0