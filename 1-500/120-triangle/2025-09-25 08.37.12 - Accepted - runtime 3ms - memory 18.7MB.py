class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        minlen = triangle[-1]

        for j in range(len(triangle)-2, -1, -1):
            for i in range(j+1):
                minlen[i] = min(minlen[i], minlen[i+1]) + triangle[j][i]
                
 
        return minlen[0]