class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diags = {}
        res = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                diag_idx = i - j
                if diag_idx not in diags:
                    diags[diag_idx] = []
                diags[diag_idx].append(grid[i][j])
        
        for k in diags:
            if k >= 0:
                diags[k].sort(reverse=True)
            else:
                diags[k].sort()
        
        for i in range(n):
            for j in range(n):
                diag_idx = i - j
                res[i][j] = diags[diag_idx].pop(0)
        

        return res