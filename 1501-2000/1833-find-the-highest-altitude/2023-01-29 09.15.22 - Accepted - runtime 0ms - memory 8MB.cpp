class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        vector<int> b={0};
        int x=0;
        for (int i=0;i<gain.size();i++){
            b.push_back(x+gain[i]);
            x+=gain[i];
        }
        return *max_element(b.begin(),b.end());
    }
};

        // b=[0]
        // x=0
        // for i in range(0,len(gain)):
        //     b.append(x+gain[i])
        //     x=x+gain[i]
        // return max(b)