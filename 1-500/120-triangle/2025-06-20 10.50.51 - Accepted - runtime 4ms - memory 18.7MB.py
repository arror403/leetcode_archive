class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        minlen = triangle[-1]

        for l in range(n-2, -1, -1):
            for i in range(l+1):
                minlen[i] = min(minlen[i], minlen[i+1]) + triangle[l][i]
            
        
        return minlen[0]