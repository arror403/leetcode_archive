class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> result;
        vector<int> current_combination;
        backtrack(result, current_combination, 1, n, k);
        return result;
    }


    void backtrack(vector<vector<int>>& result, vector<int>& current_combination, int start, int n, int k) {
        if (k == 0) {
            result.push_back(current_combination);
            return;
        }

        for (int i = start; i <= n - k + 1; ++i) {
            current_combination.push_back(i);
            backtrack(result, current_combination, i + 1, n, k - 1);
            current_combination.pop_back();
        }
    }
};