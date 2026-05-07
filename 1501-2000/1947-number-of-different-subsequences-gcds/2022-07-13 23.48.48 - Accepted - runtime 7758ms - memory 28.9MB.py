class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        biggest = max(nums)+1
        seen = [False]*biggest
        for x in nums:
            seen[x] = True

        ans = 0

        for j in range(1, biggest):
            running_gcd = 0
            for x in range(j, biggest, j):
                if seen[x]:
                    running_gcd = math.gcd(running_gcd, x)
                    if running_gcd == j:
                        break
            ans += (running_gcd == j)

        return ans