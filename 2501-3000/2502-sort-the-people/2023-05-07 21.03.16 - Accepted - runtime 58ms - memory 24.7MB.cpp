class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        vector<vector<int>> t;
        vector<string> res;
        for (int i = 0; i < names.size(); i++) {
            vector<int> tmp = {i, heights[i]};
            t.push_back(tmp);
        }
        sort(t.begin(), t.end(), [](vector<int>& a, vector<int>& b) {return a[1] > b[1];});
        for (auto i : t) {
            res.push_back(names[i[0]]);
        }
        return res;
    }
};