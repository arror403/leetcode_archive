class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        L=len(pref)

        return sum(1 for w in words if (len(w)>=L and w[:L]==pref))