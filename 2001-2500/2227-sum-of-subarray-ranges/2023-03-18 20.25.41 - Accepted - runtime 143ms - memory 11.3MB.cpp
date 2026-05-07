class Solution {
public:
    long long subArrayRanges(vector<int>& nums) {
        vector<long long> tmp;
        long long int res=0,l,r;
        for(auto i:nums){
            tmp.push_back(i);
        }

        for (int i=0;i<nums.size();i++){
            l=nums[i];
            r=nums[i];
            for(int j=i+1;j<nums.size();j++){
                l=min(l,tmp[j]);
                r=max(r,tmp[j]);
                res+=(r-l);
            }
        }
        return res;
    }
};

        // res=0
        // for i in range(len(nums)):
        //     l, r=nums[i], nums[i]
        //     for j in range(i+1,len(nums)):
        //         l = min(l,nums[j])
        //         r = max(r,nums[j])
        //         res+=(r-l)
        // return res