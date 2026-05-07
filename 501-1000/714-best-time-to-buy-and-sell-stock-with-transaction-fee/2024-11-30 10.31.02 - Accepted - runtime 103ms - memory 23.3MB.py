class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        T_ik0 = 0
        T_ik1 = -inf
        
        for p in prices:
            T_ik0_old = T_ik0
            T_ik0 = max(T_ik0, T_ik1 + p)
            T_ik1 = max(T_ik1, T_ik0_old - p - fee)


        return T_ik0