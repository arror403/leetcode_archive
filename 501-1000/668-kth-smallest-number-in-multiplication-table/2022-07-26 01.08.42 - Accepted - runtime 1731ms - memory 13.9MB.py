class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # arr = [[i*j for i in range(1,n+1)] for j in range(1,m+1)]
        # arr = reduce(lambda x,y :x+y ,arr)
        # return sorted(arr)[k-1]
        low, high = 1, m*n+1
        
        while low < high:
            mid = low + (high-low)//2
            c=self.count(mid, m, n)
            if c >= k:
                high=mid
            else:
                low=mid+1
        return high
        
    
    def count(self, v, m, n): 
        count = 0
        # for (int i = 1; i <= m; i++) 
        for i in range(1,m+1):
            temp = min(v//i,n)
            count += temp
        return count
