class Solution {
public:
    int tribonacci(int n) {
        vector<long long> b={0,1,1};
        for (int i=3;i<=38;i++){
            b.push_back(b[i-1]+b[i-2]+b[i-3]);
        }
        return (b[n]);
    }
};