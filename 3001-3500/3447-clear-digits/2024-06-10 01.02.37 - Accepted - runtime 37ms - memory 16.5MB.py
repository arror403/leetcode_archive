class Solution:
    def clearDigits(self, s: str) -> str:
        h=0
        while s.isalnum():
            h+=1
            if h>50: break
            for i,c in enumerate(s):
                if c.isdigit():
                    s=s.replace(s[i-1]+c,'')
                    break
 
        return s