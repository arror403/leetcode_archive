class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> r,res;
        int x;
        r=comb(9,k);
        // for (auto i:r){
        //     for (auto j:i){
        //         cout << j << " ";
        //     }
        //     cout << endl;
        // }
        for (auto i:r){
            x=0;
            for (auto j:i){
                x+=j;
            }
            if (x==n) res.push_back(i);
        }

        return res;
    }
    vector<vector<int>> comb(int m, int n) {
        vector<int> list,tmp;
        vector<vector<int>> res;
        for (int i = 0; i < n; ++i){
            list.push_back(i);
        }
        --list[n - 1];
        do {
            for (int i = n - 1; i >= 0; --i) {
                if (list[i] < m + i - n) {
                    ++list[i];
                    for (int j = i + 1; j < n; ++j) {
                        list[j] = list[i] + j - i;
                    }
                    break;
                }
            }
            tmp.clear();
            for (int i = 0; i < n; ++i) {
                // cout << list[i] + 1 << '\t';
                tmp.push_back(list[i] + 1);
            }
            res.push_back(tmp);
            // cout << endl;
        } while (list[0] < (m - n));
        return res;
    }    
};