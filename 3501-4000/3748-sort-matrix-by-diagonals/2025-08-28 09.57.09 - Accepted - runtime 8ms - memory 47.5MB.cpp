class Solution {
public:
    vector<vector<int>> sortMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        unordered_map<int, vector<int>> diags;
        vector<vector<int>> res(n, vector<int>(n, 0));
        
        // Collect elements by diagonal
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int diag_idx = i - j;
                diags[diag_idx].push_back(grid[i][j]);
            }
        }
        
        // Sort each diagonal
        for (auto& [k, diagonal] : diags) {
            if (k >= 0) {
                sort(diagonal.rbegin(), diagonal.rend()); // descending
            } else {
                sort(diagonal.begin(), diagonal.end()); // ascending
            }
        }
        
        // Place sorted elements back
        unordered_map<int, int> indices; // Track current index for each diagonal
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int diag_idx = i - j;
                res[i][j] = diags[diag_idx][indices[diag_idx]++];
            }
        }
        
        return res;
    }
};

// class Solution {
// public:
//     vector<vector<int>> sortMatrix(vector<vector<int>>& grid) {
//         int n = grid.size(), diag_idx;
//         unordered_set<int> diags;
//         vector<vector<int>> res;
//         vector<int> tmp;

//         for (int i=0; i<n; i++) tmp.push_back(0);

//         for (int i=0; i<n; i++) res.push_back(tmp);
        
//         for (int i=0; i<n; i++){
//             for (int j=0; j<n; j++){
//                 diag_idx = i - j;
//                 if (auto search = diags.find(diag_idx); search == diags.end()){
//                     diags[diag_idx].erase(diag_idx);
//                 }
//                 diags[diag_idx].insert(grid[i][j]);
//             }
//         }

//         for (auto k:diags){
//             if (k>=0) {
//                 diags[k].sort();
//                 diags[k].reverse();
//             }
//             else diags[k].sort();
//         }

        
//         for (int i=0; i<n; i++){
//             for (int j=0; j<n; j++){
//                 diag_idx = i - j;
//                 if (auto search = diags.find(diag_idx); search != diags.end()){
//                     res[i][j]=0;
//                     diags[diag_idx].erase(0);
//                 }
//             }
//         }

//         return res;   
//     }
// };