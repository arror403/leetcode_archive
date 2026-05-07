class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res=numBottles
        while numBottles >= numExchange:
            res+=numBottles//numExchange
            numBottles=sum(divmod(numBottles,numExchange))
        return res