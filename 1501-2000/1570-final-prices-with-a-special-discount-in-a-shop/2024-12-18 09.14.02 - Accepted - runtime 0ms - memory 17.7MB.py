class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = [] #prices without discount
        res = prices[:]

        for i,v in enumerate(prices):
            while stack and prices[stack[-1]] >= v:
                res[stack.pop()] -= v

            stack.append(i)


        return res