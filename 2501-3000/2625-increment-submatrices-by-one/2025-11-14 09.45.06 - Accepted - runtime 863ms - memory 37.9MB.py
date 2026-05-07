class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        res = [[0]*n for _ in range(n)]

        for a, b, x, y in queries:
            for i in range(a, x+1):
                res[i][b] += 1
                if y+1 < n: 
                    res[i][y+1] -= 1
        
        for i in range(n):
            for j in range(1, n):
                res[i][j] += res[i][j-1]


        return res