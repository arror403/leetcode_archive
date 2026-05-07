class Solution {
public:
    bool isPowerOfFour(int n) {
        double x=log(n)/log(4);

        if (n<=0) return false;

        return n==pow(4, round(x));
    }
};