class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min=INT_MAX;
        int max=0;
        for (auto i:prices){
            if (i<min) 
                min=i;
            else if ((i-min)>max) 
                max=i-min;
        }
        return max;
    }
};


        // min=100000
        // max=0
        // for i in prices:
        //     if(i<min):
        //         min=i
        //     elif(i-min)>max:
        //         max=i-min
        // return max