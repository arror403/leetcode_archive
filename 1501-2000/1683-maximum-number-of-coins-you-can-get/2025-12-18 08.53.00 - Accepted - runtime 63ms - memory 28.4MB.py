class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        d=deque(sorted(piles))
        res=0

        while d:
            d.popleft()
            d.pop()
            res+=d.pop()


        return res