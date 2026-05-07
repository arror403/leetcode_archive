class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int output = 0;
        for(int i=0;i<nums.size();i++){
            for(int j=i+1;j<nums.size();j++){
                if (nums[i]==nums[j]) output++;
            }
        }
        return output;
    }
};



        // output=0
        // for i in range(0,len(nums)):
        //     for j in range(i+1,len(nums)):
        //         if nums[i]==nums[j]:
        //             output+=1
        
        // return output