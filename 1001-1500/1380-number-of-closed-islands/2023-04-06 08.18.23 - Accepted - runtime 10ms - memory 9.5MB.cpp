class Solution {
public:
    int closedIsland(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int res = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0 && dfs(grid, i, j)) {
                    res++;
                }
            }
        }
        return res;
    }
    

    bool dfs(vector<vector<int>>& grid, int i, int j) {
        if (i < 0 || i >= grid.size() || j < 0 || j >= grid[0].size()) {
            return false;
        }
        if (grid[i][j] == 1) {
            return true;
        }
        grid[i][j] = 1;
        bool res = true;
        res &= dfs(grid, i+1, j);
        res &= dfs(grid, i-1, j);
        res &= dfs(grid, i, j+1);
        res &= dfs(grid, i, j-1);
        return res;
    }        
};