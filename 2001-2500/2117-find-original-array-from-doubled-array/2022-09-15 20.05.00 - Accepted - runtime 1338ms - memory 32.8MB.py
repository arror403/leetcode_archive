class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        c = collections.Counter(changed)
        if c[0]%2: return []
        for i in sorted(c):
            if c[i] > c[2*i]:
                return []
            c[2*i]-=c[i] if i else c[i]//2
        return list(c.elements())