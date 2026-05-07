class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        res=0
        d=deque(sorted(nums))

        while d:
            d.pop()
            res+=d.pop()
            d.popleft()


        return res