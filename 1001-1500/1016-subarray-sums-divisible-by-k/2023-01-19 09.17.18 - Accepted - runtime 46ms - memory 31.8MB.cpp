class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        return subCount(nums,k); 
    }
    int subCount(vector<int> arr,int k){
        int n=arr.size();

        vector<int> mod;
        for (int i=0;i<=k;i++){
            mod.push_back(0);
        }
    
        int cumSum = 0;
        for (int i=0;i<n;i++){
            cumSum = cumSum + arr[i];
            mod[((cumSum % k)+k)% k] = mod[((cumSum % k)+k)% k] + 1;
        }

        int result = 0;
        for (int i=0;i<k;i++){
            if (mod[i] > 1)
                result = result + int((mod[i]*(mod[i]-1))/2);
        }        

        result = result + mod[0];
        
        return result;
    }    
};