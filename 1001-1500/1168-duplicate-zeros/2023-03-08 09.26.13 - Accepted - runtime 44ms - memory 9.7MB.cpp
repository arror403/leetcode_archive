class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        int z=0,i=0,b;
        // auto it;
        for (int i:arr){
            if (i==0) z++;
        }
        b=arr.size();
        while (1){
            if (arr[i]==0){
                arr.insert(arr.begin() + i, 0);
                i++;
            }
            i++;
            if ((b+z)==arr.size()) break;
        }
        for (int i=0;i<z;i++){
            arr.pop_back();
        }
    }
};