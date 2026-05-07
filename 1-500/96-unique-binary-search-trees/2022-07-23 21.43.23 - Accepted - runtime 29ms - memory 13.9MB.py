class Solution:
    def numTrees(self, n: int) -> int:
        # res=[1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845, 35357670, 129644790, 477638700, 1767263190]
        
        return int(self.combination(2*n,n)/(n+1))
    
    
    def combination(self, n, r):
        result=1
        p=n
        q=1
        for i in range(r):
            result=result*p
            p=p-1
            result=result/q
            q=q+1

        return int(result)