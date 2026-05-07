class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        largest_k = heapq.nlargest(k, enumerate(nums), key=lambda x: x[1])
        return [v for i, v in sorted(largest_k)]