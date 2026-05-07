class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        m = [i for i, v in enumerate(nums) if v]

        for a, b in pairwise(m):
            if (b - a) <= k:
                return False

        return True