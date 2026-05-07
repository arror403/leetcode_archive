class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int t=numBottles;
        while (numBottles >= numExchange){
            t+=int(numBottles/numExchange);
            numBottles=int(numBottles/numExchange)+numBottles%numExchange;
        }

        return t;
    }
};