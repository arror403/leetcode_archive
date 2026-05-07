class Solution:
    def sumCounts(self, n: List[int]) -> int:
        t=[n[i:j] for i in range(len(n)) for j in range(i+1, len(n)+1)]
        # return sum([len(set(x))**2 for x in t])
        res=0
        for x in t: res+=len(set(x))**2
        return res