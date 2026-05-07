class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        La, Lb = len(nums1), len(nums2)
        # sa = [nums1[i:j] for i in range(La) for j in range(i+1, La+1)]
        # sb = [nums2[i:j] for i in range(Lb) for j in range(i+1, Lb+1)]
        dp = [[0]*Lb for _ in range(La)]

        for i in range(La):
            for j in range(Lb):
                dp[i][j] = nums1[i] * nums2[j]
                if i and j: dp[i][j] += max(dp[i-1][j-1], 0)
                if i: dp[i][j] = max(dp[i][j], dp[i-1][j])
                if j: dp[i][j] = max(dp[i][j], dp[i][j-1])
        # print(dp)

        return dp[-1][-1]