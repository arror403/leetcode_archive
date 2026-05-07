class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        vector <int>b;
        for (int i=0;i<nums.size();i++) b.push_back(nums[nums[i]]);
        return b;
    }
};