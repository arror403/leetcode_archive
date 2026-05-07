class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        d=[[i,v] for i,v in enumerate(nums)]
        return [q[1] for q in sorted(sorted(d, key=lambda x:x[1], reverse=1)[:k], key=lambda x:x[0])]