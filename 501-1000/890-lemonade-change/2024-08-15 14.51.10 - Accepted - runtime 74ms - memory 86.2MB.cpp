class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int ten=0,five=0;

        for (int v:bills){
            if (v==5)
                five++;
            else if (v==10){
                if (five==0) return false;
                ten++;
                five--;
            }
            else {
                if (ten>0 && five>0){
                    ten--;
                    five--;
                }
                else if (five>=3)
                    five-=3;
                else
                    return false;
            }
        }

        return true;
    }
};