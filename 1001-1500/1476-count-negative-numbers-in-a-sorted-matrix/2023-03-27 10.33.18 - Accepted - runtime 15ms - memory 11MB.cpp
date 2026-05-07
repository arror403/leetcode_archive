class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int sum=0;
        for (auto r:grid){
            for (auto c:r){
                if (c<0) sum++;
            }
        }
        return sum;
    }
};