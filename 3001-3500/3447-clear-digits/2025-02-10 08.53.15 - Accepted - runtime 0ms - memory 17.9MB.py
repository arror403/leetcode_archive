class Solution:
    def clearDigits(self, s: str) -> str:
        d=[]

        for c in s:
            if c.isalpha():
                d.append(c)
            else:
                d.pop()

        return ''.join(d)