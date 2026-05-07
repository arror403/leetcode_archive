class Solution {
public:
    int arraySign(vector<int>& nums) {
        double t=1.0;
        for (int i:nums) t*=i;
        if (t<0) return -1;
        else if (t>1) return 1;
        else return 0; 
    }
};