class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return (heapq.nlargest(2,nums)[0]-1)*(heapq.nlargest(2,nums)[1]-1)