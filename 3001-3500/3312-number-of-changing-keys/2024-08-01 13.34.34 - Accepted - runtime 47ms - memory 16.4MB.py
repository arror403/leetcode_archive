class Solution:
    def countKeyChanges(self, s: str) -> int:
        return len([a for a,b in pairwise(s) if (ord(a)-ord(b)) not in (0,32,-32)])