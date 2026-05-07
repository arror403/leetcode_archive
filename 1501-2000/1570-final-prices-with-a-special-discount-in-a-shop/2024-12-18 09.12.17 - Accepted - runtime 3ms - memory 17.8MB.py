class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        L=len(prices)
        for i in range(L):
            for j in range(i+1, L):
                if prices[j]<=prices[i]:
                    prices[i]-=prices[j]
                    break
        
        
        return prices