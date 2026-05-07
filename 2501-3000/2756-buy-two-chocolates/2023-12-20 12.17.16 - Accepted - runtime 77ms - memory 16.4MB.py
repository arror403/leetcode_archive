class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
            res=money-sum(nsmallest(2, prices))

            return res if res >= 0 else money