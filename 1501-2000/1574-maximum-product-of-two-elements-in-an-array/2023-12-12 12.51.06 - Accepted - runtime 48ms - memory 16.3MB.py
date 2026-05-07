class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return (l := heapq.nlargest(2, nums))[0]*l[1] -l[0]-l[1] +1
