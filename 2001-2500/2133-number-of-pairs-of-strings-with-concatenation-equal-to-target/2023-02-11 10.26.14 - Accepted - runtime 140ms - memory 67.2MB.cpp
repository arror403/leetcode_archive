class Solution {
public:
    int numOfPairs(vector<string>& nums, string target) {
        int t=0;
        for (int i=0;i<nums.size();i++){
            for(int j=i+1;j<nums.size();j++){
                if (nums[i]+nums[j]==target) t++;
                if (nums[j]+nums[i]==target) t++;
            }
        }
        return t;
    }
};
