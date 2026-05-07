class Solution {
public:
    int findLucky(vector<int>& arr) {
        vector<int> res;
        for (auto i:arr){
            if (i==count(arr.begin(), arr.end(), i))
                res.push_back(i);
        }
        if (res.size()!=0) return *max_element(res.begin(),res.end());
        else return -1;
    }
};