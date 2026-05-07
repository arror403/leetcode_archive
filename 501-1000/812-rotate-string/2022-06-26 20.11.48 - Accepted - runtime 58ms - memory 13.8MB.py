class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        c=[]
        for i in range(len(s)):
            s=s[1:]+s[:1]
            c.append(s)
        
        if goal in c:
            return 1
        else: 
            return 0