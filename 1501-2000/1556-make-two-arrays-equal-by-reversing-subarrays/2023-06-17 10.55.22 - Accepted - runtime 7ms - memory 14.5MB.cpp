class Solution {
public:
    bool canBeEqual(vector<int>& target, vector<int>& arr) {
        sort(target.begin(),target.end());
        sort(arr.begin(),arr.end());
        int ans=1;
        for (int i=0;i<arr.size();i++){
            if (target[i]!=arr[i]){
                ans=0;
                break;
            }
        }
        return ans;
    }
};

        // target.sort()
        // arr.sort()
        // ans=1
        // for i in range(0,len(arr)):
        //     if target[i]!=arr[i]:
        //         ans=0
        //         break
                
        // return ans