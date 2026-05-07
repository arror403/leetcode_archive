class Solution {
public:
    int trailingZeroes(int n) {
        if (n==0) return 0;
        int res=0,k=log_a_to_base_b(n,5);
        for (int i=1;i<=k+1;i++) res+=int(n/pow(5,i));
        return res;
    }
    int log_a_to_base_b(int a, int b){
        return log2(a) / log2(b);
    }
};

        // if n==0: return 0
        // k,res=int(math.log(n,5)),0
        // for i in range(1,k+1): res+=int(n/(5**i))
        // return res