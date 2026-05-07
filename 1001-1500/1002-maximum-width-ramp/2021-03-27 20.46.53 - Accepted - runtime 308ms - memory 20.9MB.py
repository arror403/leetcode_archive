class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        b=0
        m=50000
        
        for i in sorted(range(len(A)), key=A.__getitem__):
            b=max(b,i-m)
            m=min(m,i)
        return b