class Solution:
    def countPrefixSuffixPairs(self, w: List[str]) -> int:
        L=len(w)
        res=0
        for i in range(L):
            for j in range(i+1,L):
                if w[j].endswith(w[i]) and w[j].startswith(w[i]):
                    res+=1
                    
        return res