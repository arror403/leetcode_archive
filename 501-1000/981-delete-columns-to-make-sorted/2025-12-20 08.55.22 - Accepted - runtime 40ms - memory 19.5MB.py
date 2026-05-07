class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        t=list(zip(*[list(s) for s in strs]))

        return len([s for s in t if list(s)!=sorted(s)])