class Solution {
public:
    bool isPerfectSquare(int num) {
        double u=sqrt(num);
        return int(u)*int(u)==num;
    }
};
