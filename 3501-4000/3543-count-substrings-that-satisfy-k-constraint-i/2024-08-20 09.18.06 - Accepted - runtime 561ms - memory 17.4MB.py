class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        L=len(s)
        m=[Counter(s[i:j]) for i in range(L) for j in range(i+1, L+1)]

        return sum(1 for d in m if d['0']<=k or d['1']<=k)