class Solution {
public:
    int triangularSum(vector<int>& nums) {
        vector <int> tmp;
        while (nums.size()>1){
            tmp.clear();
            for(int i=1;i<nums.size();i++){
                tmp.push_back((nums[i]+nums[i-1])%10);
            }
            nums=tmp;
        }
        return nums[0];
    }
};


        // while len(nums)>1:
        //     tmp=[]
        //     for i in range(1,len(nums)):
        //         tmp.append((nums[i]+nums[i-1])%10)
        //         # print(tmp)
        //     nums=tmp
            
            
        // return nums[0]