class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        L = len(nums)
        ans = 0
        
        for i in range(L):
            # Skip if remaining length can't beat ans
            if L - i <= ans: break
            
            evens = set()
            odds = set()
            for j in range(i, L):
                if nums[j] % 2 == 0:
                    evens.add(nums[j])
                else:
                    odds.add(nums[j])
                if len(evens) == len(odds):
                    ans = max(ans, j - i + 1)


        return ans