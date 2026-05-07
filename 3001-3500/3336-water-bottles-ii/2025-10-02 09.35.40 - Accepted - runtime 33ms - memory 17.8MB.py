class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        bottle = numBottles

        while bottle >= numExchange:
            bottle -= numExchange
            numExchange += 1
            res += 1
            bottle += 1
    

        return res