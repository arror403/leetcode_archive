class Solution:
    def reverseByType(self, s: str) -> str:
        a=[[],[]]
        for c in s: a[c.isalpha()]+=[c]

        return ''.join([a[c.isalpha()].pop() for c in s])