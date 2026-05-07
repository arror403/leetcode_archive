class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> b;
        int index = n;
        for(int i=0;i<n;i++){
            b.push_back(nums[i]);
            b.push_back(nums[index]);
            index++;
        }
        return b;
    }
};

        // b=[]
        // index=n
        // for i in range(0,n):
        //     b.append(nums[i])
        //     b.append(nums[index])
        //     index+=1
            
        // return b