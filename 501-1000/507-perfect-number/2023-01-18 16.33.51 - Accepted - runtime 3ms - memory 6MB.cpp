class Solution {
public:
    bool checkPerfectNumber(int num) {
        bool flag=0;
        if (num==6)flag=1;
        else if (num==28)flag=1;
        else if (num==496)flag=1;
        else if (num==8128)flag=1;
        else if (num==33550336)flag=1;
        return flag;
    }
};

