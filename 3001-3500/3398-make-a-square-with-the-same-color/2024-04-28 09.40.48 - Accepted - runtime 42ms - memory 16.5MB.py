class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:

        def get_2x2_matrices(m):
            res=[]
            for i in range(2):
                for j in range(2):
                    res.append(''.join(sorted(m[i][j]+m[i][j+1]+m[i+1][j]+m[i+1][j+1])))
            return res


        for t in get_2x2_matrices(grid):
            if t in ["BBBW","BWWW","BBBB","WWWW"]:
                return True


        return False