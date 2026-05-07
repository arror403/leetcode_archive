class Solution:
    def accountBalanceAfterPurchase(self, p: int) -> int:
        if p%10==0: return 100-p
        a,b=p-(p//10)*10,(p//10+1)*10-p

        if a>=b:
            return 100-(p//10+1)*10
        # elif a==b:
        #     return 
        else: 
            return 100-(p//10)*10