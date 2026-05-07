class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        unordered_map<int, int> d={{5,0}, {10,0}};

        for (auto v:bills){
            if (v==5)
                d[5]++;
            else if (v==10){
                if (d[5]==0) return false;
                d[10]++;
                d[5]--;
            }
            else {
                if (d[10]>0 && d[5]>0){
                    d[10]--;
                    d[5]--;
                }
                else if (d[5]>=3)
                    d[5]-=3;
                else
                    return false;
            }
        }

        return true;
    }
};