class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int l=(mat[0]).size();
        // cout << l;
        int sum=0;
        for (int i=0;i<l;i++) sum+=mat[i][i];
        for (int i=l-1;i>=0;i--){
            if ((l-i-1)!=i){
                sum+=mat[l-i-1][i];
            }
        }
        return sum;
    }
};

        // l=len(mat[0])
        // sum=0
        // for i in range(l): sum+=mat[i][i]
        
        // for i in range(l-1,-1,-1):
        //     if (l-i-1)!=i:
        //         sum+=mat[l-i-1][i]

        // return sum