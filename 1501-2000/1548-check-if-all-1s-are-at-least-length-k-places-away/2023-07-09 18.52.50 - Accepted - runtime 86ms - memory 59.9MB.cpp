class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        vector<int> m;
        bool f=true;

        for (int i=0;i<nums.size();i++){
            if (nums[i]==1) m.push_back(i);
        }

        for (int i=1;i<m.size();i++){
            if ((m[i]-m[i-1]-1)>=k) continue;
            else{
                f=false;
                break;
            }
        }
        return f;      
    }
};