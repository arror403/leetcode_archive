class Solution:
    def minPartitions(self, n: str) -> int:
        n=list(n)
        
        for i in range(len(n)):
            n[i]=int(n[i])
            
        return max(n)