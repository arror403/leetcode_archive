class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> cur;
        for(int i=0;i<n;i++) cur.push_back(1);
        for(int i=1;i<m;i++){
            for(int j=1;j<n;j++){
                cur[j] += cur[j-1];
            }
        }
        return cur[n-1];
    }
};

        // cur=[1]*n
        // for i in range(1,m):
        //     for j in range(1,n):
        //         cur[j] += cur[j-1]
                
        // return cur[n-1]