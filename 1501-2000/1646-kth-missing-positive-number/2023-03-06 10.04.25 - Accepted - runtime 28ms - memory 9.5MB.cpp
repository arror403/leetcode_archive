class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int t=1,y=0;
        bool f;
        while (1){
            f=1;
            for (auto i:arr){
                if (i==t){
                    f=0;
                    break;
                }
            }
            if (f)
                y+=1;
            if (y==k)
                break;
            t++;
        }
        return t;  
    }
};