class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        vector<int> b;
        for (int i=0;i<nums.size();i++){
            if (nums[i]%2==0) b.push_back(nums[i]);
        }
        for (int i=0;i<nums.size();i++){
            if (nums[i]%2==1) b.push_back(nums[i]);
        }
        return b;
    }
};

        // b=[]
        // for i in A:
        //     if i%2==0:
        //         b.append(i)
        // for i in A:
        //     if i%2==1:
        //         b.append(i)
                
        // return b