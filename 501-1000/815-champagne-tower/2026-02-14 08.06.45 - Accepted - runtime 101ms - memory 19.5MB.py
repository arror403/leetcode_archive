class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [[0]*(i+1) for i in range(query_row+1)]
        glasses[0][0] = poured
        
        for r in range(query_row):
            for c in range(len(glasses[r])):
                overflow = max(0, glasses[r][c]-1) / 2
                glasses[r+1][c] += overflow
                glasses[r+1][c+1] += overflow
        

        return min(1, glasses[query_row][query_glass])