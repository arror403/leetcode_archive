class Solution {
public:
    vector<int> sortEvenOdd(vector<int>& nums) {
        vector<int>odd,even,res;
        for (int i=0;i<nums.size();i++){
            if (i%2==0)
                even.push_back(nums[i]);
            else
                odd.push_back(nums[i]);
        }
        sort(odd.begin(),odd.end());
        reverse(odd.begin(),odd.end());
        sort(even.begin(),even.end());

        int t;
        t=min(odd.size(),even.size());
        for (int i=0;i<t;i++){
            res.push_back(even[i]);
            res.push_back(odd[i]);
        }
        if (odd.size()>even.size())
            res.push_back(odd[odd.size()-1]);
        else if (odd.size()<even.size())
            res.push_back(even[even.size()-1]);

        return res;
    }
};