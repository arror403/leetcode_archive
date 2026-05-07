class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k>len(s): return False

        odd_count=sum(v%2==1 for v in Counter(s).values())
        
        return odd_count <= k <= len(s)