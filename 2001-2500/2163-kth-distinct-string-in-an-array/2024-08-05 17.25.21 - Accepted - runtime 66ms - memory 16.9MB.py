class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d=[v for v,f in Counter(arr).items() if f==1]
        
        return "" if k>len(d) else d[k-1]