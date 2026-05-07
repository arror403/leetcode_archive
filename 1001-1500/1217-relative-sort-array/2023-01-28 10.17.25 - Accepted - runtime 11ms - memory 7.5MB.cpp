class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        vector<int> b,tmp;
        for (auto i: arr2){
            for(auto j: arr1){
                if (i==j) b.push_back(j);
            }
        }
        bool f1;
        for (auto i: arr1){
            f1=false;
            for (auto x: b){
                if (i==x){
                    f1=true;
                    break;
                }
            }
            if (f1==false) tmp.push_back(i);
        }
        sort(tmp.begin(),tmp.end());
        for (auto i: tmp) b.push_back(i);
        return b;
    }
};