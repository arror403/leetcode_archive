class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        // int M = max(candies);
        int M=-1;
        vector<bool> output;
        for (int i = 0; i < candies.size(); i++)
            if (candies[i]>M) M=candies[i];
        
        
        for (int i=0;i<candies.size();i++){
            if ((candies[i]+extraCandies)>=int(M)) output.push_back(1);
            else output.push_back(0);
        }
        return output;
    }
};


        // M = max(candies)
        // output=[]
        // for i in range(0,len(candies)):
        //     if (candies[i]+extraCandies)>=M:
        //         # print((candies[i]+extraCandies))
        //         output.append(1)
        //     else:
        //         output.append(0)
            
        // return output