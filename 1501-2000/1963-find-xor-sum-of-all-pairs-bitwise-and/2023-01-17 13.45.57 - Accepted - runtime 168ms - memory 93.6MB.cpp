class Solution {
public:
    int getXORSum(vector<int>& arr1, vector<int>& arr2){
        int r1=0,r2=0;
        for(int i =0 ; i < arr1.size(); i++)
            r1 = r1 ^ arr1[i];
        for(int i =0 ; i < arr2.size(); i++)
            r2 = r2 ^ arr2[i];
        // auto arr1XorSum = accumulate(arr1.begin(),arr1.end(),xor<int>());
        // auto arr2XorSum = accumulate(arr2.begin(),arr2.end(),xor<int>());
        return r1 & r2;
    }
};

        // arr2XorSum = reduce(lambda a,b: a^b, arr2)
        
        // arr1XorSum = reduce(lambda a,b: a^b, arr1)
        
        // return arr1XorSum & arr2XorSum