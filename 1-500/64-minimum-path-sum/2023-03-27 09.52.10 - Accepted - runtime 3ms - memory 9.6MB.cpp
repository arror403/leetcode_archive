class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int c=grid.size(),r=grid[0].size();
        for (int i=1;i<c;i++){
            grid[i][0]+=grid[i-1][0];
        }
        for (int j=1;j<r;j++){
            grid[0][j]+=grid[0][j-1];
        }
        for (int i=1;i<c;i++){
            for (int j=1;j<r;j++){
                grid[i][j]+=min(grid[i-1][j],grid[i][j-1]);
            }
        }
        return grid[c-1][r-1];
    }
};