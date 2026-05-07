class Solution {
public:
    int findSpecialInteger(vector<int>& arr) {
        vector<vector<int>> res;
        vector<int> current;
        for (int i = 0; i < arr.size(); i++) {
            if (i == 0 || arr[i] == arr[i - 1]) {
                current.push_back(arr[i]);
            } else {
                res.push_back(current);
                current = {arr[i]};
            }
        }
        res.push_back(current);

        int len_arr = arr.size();
        for (vector<int>& i : res) {
            if (static_cast<double>(i.size()) / len_arr > 0.25) {
                return i[0];
            }
        }

        // Return -1 or some other value to indicate failure or not found
        return -1;
    }
};