class Solution:
    def accountBalanceAfterPurchase(self, p: int) -> int:
        # if p%10 == 0: return 100 - p
        # r=(p//10)

        # if (p-r*10) >= (r+1)*10-p:
        #     return 100 - (r+1)*10
        # else: 
        #     return 100 - r*10
        return 100 - ((p + 5) // 10) * 10