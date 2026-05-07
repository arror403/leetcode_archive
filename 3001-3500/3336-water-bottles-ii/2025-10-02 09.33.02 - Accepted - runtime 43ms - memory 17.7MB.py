class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        full_bottle, empty_bottle, res = numBottles, 0, 0

        while full_bottle:
            res += full_bottle
            empty_bottle += full_bottle
            full_bottle = 0
            
            while empty_bottle >= numExchange:
                empty_bottle -= numExchange
                numExchange += 1
                full_bottle += 1


        return res