class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& nums) {
        vector<int> odd,even,res;
        int e=0,o=0;
        for (auto i: nums){
            if (i%2==0) even.push_back(i);
            else odd.push_back(i);
        }
        for (int i=0;i<nums.size();i++){
            if (i%2==0){ 
                res.push_back(even[e]);
                e+=1;
            }
            else{
                res.push_back(odd[o]);
                o+=1;
            }            
        }
        return res;
    }
};