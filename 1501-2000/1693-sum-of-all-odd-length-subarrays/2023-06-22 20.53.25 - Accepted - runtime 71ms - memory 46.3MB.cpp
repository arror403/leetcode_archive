class Solution {
public:
    int sumOddLengthSubarrays(vector<int>& arr) {
        int t = 0;
        vector<vector<int>> b = sub_lists(arr);
        for (auto& i : b) {
            if (i.size() % 2 == 1) {
                t += sum(i);
            }
        }
        return t;
    }

    vector<vector<int>> sub_lists(vector<int>& l) {
        vector<vector<int>> lists;
        for (size_t i = 0; i < l.size() + 1; i++) {
            for (size_t j = 0; j < i; j++) {
                lists.push_back(vector<int>(l.begin() + j, l.begin() + i));
            }
        }
        return lists;
    }

    int sum(vector<int>& nums) {
        int total = 0;
        for (auto& num : nums) {
            total += num;
        }
        return total;
    }
};