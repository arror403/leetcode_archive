class Solution:
    def maximumHappinessSum(self, h: List[int], k: int) -> int:
        h.sort(reverse=True)

        for i in range(1,k):
            if h[i]<i:
                return sum(h[:i])-(i*(i-1)//2)

        return sum(h[:k])-(k*(k-1)//2)