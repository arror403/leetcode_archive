class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int tmp=0;
        vector<int> b;
        if ((nums.size()==1)&&(nums[0]==1)) b.push_back(1);
        else {
            for (int i=0;i<nums.size();i++){
                if (nums[i]==1){
                    tmp++;
                    b.push_back(tmp);
                }
                else if(nums[i]==0) tmp=0;
            }
        }
        if (b.size()==0) return 0;
        else return *max_element(b.begin(), b.end());
    }
};

        // tmp=0
        // b=[]
        // if (len(nums)==1)&(nums[0]==1):
        //     b.append(1)
        // else:
        //     for i in nums:
        //         if i==1:
        //             tmp+=1
        //             b.append(tmp)
        //         elif i==0:
        //             tmp=0
                
        // if len(b)==0:return 0
        
        // else: return (max(b))