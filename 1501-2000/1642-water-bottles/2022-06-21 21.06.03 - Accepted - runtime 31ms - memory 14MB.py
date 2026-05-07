class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        t=numBottles
        while numBottles >= numExchange:
            t+=int(numBottles/numExchange)
            numBottles=int(numBottles/numExchange)+numBottles%numExchange
        return t