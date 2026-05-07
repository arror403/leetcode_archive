class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int res = numBottles;

        while (numBottles >= numExchange){
            res += int(numBottles / numExchange);
            numBottles = int(numBottles / numExchange) + numBottles % numExchange;
        }


        return res;
    }
};