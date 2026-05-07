class Solution:
    def largestEven(self, s: str) -> str:
        t=list(s)

        while t and t[-1]=='1':
            t.pop()

        
        return ''.join(t)