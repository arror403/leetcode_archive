class Solution:
    def twoEggDrop(self, n: int) -> int:
        drops=floors=0
        
        while floors<n:
            drops+=1
            floors+=drops
        
        return drops