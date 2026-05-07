class Solution {
public:
    int pivotInteger(int n) {
        int x=pow(n,2)+n;
        for(int i=1;i<n+1;i++){
            if (2*pow(i,2)==x){
                return i;
            }
        }
        return -1;     
    }
};