class Solution:
    def countPrefixSuffixPairs(self, w: List[str]) -> int:
        L=len(w)

        return sum((w[j].endswith(w[i]) and w[j].startswith(w[i])) for i in range(L) for j in range(i+1,L))