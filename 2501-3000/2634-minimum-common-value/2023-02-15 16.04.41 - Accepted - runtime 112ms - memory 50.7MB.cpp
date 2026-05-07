class Solution {
public:
    int getCommon(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;
        set_intersection(nums1.begin(),nums1.end(),
                          nums2.begin(),nums2.end(),
                          back_inserter(res));
        sort(res.begin(),res.end());
        if (res.size()!=0){
            return *min_element(res.begin(),res.end());
        }
        else return -1;
    }
};