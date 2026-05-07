class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        L = len(prices)
        if k >= L//2: 
            return sum([prices[i]-prices[i-1] for i in range(1,L) if prices[i]>prices[i-1]])
 
        t=[[0]*(L) for _ in range(k+1)]
        for i in range(1, k+1):
            tmpMax = -prices[0]
            for j in range(1, L):
                t[i][j] = max(t[i][j-1], prices[j] + tmpMax)
                tmpMax =  max(tmpMax, t[i-1][j-1] - prices[j])
        

        return t[k][L-1]