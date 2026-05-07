class Solution {
public:
    vector<vector<int>> sortTheStudents(vector<vector<int>>& score, int k) {
        int idx = k;
        sort(score.begin(), score.end(), [idx](const vector<int>& a, const vector<int>& b) {
            return a.at(idx) < b.at(idx);
        });
        reverse(score.begin(),score.end());
        return score;
    }
};