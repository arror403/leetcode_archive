class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        a=0
        b=len(s)
        for i in range(len(s)):
            if s[i]==letter:
                a+=1
                
        return int(a/b*100)