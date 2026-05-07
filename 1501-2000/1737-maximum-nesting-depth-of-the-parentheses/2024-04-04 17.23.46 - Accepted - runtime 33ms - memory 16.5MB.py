class Solution:
    def maxDepth(self, s: str) -> int:
        n=0
        b=[0]
        for i in s:
            if i=='(':
                n+=1
                b.append(n)
            elif i==')':
                n-=1
                b.append(n)
        return (max(b))