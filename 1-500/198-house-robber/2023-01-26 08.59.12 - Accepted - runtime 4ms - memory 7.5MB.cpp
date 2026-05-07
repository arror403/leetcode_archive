class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size()==0) return 0;
        int prev1 = 0,prev2 = 0,tmp;
        for (int num : nums){
            tmp = prev1;
            prev1 = max(prev2 + num, prev1);
            prev2 = tmp;
        }
        return prev1; 
    }
};


        // if (len(nums)==0):
        //     return 0
        // prev1 = 0
        // prev2 = 0
        // # for (int num : nums)
        // for num in nums:
        //     tmp = prev1
        //     prev1 = max(prev2 + num, prev1)
        //     prev2 = tmp
        // return prev1