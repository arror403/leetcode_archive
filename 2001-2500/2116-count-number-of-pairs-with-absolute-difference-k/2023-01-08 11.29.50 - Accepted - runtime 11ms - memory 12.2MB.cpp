class Solution {
public:
    int countKDifference(vector<int>& nums, int k) {
        int r=0;
        for (int i=0;i<nums.size();i++){
            for (int j=0;j<i;j++){
                if (abs(nums[j]-nums[i])==k)
                    r++;
            }
        }
        return r;
    }
};


        // r=0
        // for i in range(len(nums)):
        //     for j in range(i):
        //         if abs(nums[j]-nums[i])==k:
        //             r+=1
                    
        // return r