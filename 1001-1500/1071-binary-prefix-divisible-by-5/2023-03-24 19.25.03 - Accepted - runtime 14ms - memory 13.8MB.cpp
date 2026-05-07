class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& nums) {
        vector<bool> answer;
        int t=0;
        for (auto i :nums){
            t = (t*2 + i)%5;
            if (t==0) answer.push_back(true);
            else answer.push_back(false);
        }
        return answer;
    }
};