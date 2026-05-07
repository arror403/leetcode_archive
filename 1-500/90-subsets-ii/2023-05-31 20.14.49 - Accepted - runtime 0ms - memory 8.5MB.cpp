class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> res;
        vector<vector<int>> tmp;
        
        sort(nums.begin(), nums.end()); // Sort the input vector
        
        for (int i = 0; i <= nums.size(); i++) {
            vector<vector<int>> subsets = combinations(nums, i); // Get all combinations of length i
            tmp.insert(tmp.end(), subsets.begin(), subsets.end()); // Append the subsets to tmp
        }
        
        unordered_set<vector<int>, VectorHash> uniqueSubsets(tmp.begin(), tmp.end()); // Use unordered_set to remove duplicates
        
        res.insert(res.end(), uniqueSubsets.begin(), uniqueSubsets.end()); // Copy unique subsets to res
        
        return res;
    }
    
private:
    struct VectorHash {
        size_t operator()(const vector<int>& v) const {
            size_t hashValue = 0;
            for (const int& i : v) {
                hashValue ^= hash<int>()(i);
            }
            return hashValue;
        }
    };
    
    vector<vector<int>> combinations(vector<int>& nums, int k) {
        vector<vector<int>> result;
        vector<int> subset;
        backtrack(result, nums, subset, 0, k);
        return result;
    }
    
    void backtrack(vector<vector<int>>& result, vector<int>& nums, vector<int>& subset, int start, int k) {
        if (subset.size() == k) {
            result.push_back(subset);
            return;
        }
        
        for (int i = start; i < nums.size(); i++) {
            if (i > start && nums[i] == nums[i-1]) {
                continue; // Skip duplicates
            }
            subset.push_back(nums[i]);
            backtrack(result, nums, subset, i + 1, k);
            subset.pop_back();
        }
    }
};