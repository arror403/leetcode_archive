class Solution {
public:
    vector<int> constructTransformedArray(vector<int>& nums) {
        int L=nums.size();
        vector<int> res(L,0);
        int i=0;
        for(auto v:nums){
            if (v != 0) {
                // Handle negative modulo
                res[i] = nums[((i+v)%L + L)%L];
            }
            i++;
        }
        return res;
    }
};