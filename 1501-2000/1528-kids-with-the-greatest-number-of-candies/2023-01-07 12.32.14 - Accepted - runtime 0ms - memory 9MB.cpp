class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        // int M = max(candies);
        int M=-1;
        vector<bool> output;
        for (int i = 0; i < candies.size(); i++)
            if (candies[i]>M) M=candies[i];
        
        
        for (int i=0;i<candies.size();i++){
            if ((candies[i]+extraCandies)>=M) output.push_back(true);
            else output.push_back(false);
        }
        return output;
    }
};