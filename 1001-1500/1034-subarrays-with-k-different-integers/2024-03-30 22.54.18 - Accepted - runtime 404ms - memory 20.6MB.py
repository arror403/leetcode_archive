class Solution:
    ##### power by chatGPT #####
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums, k):
            count = Counter()
            left = 0
            distinct = 0
            res = 0

            for right in range(len(nums)):
                if count[nums[right]] == 0:
                    distinct += 1
                count[nums[right]] += 1

                while distinct > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        distinct -= 1
                    left += 1

                res += right - left + 1

            return res

        return atMostK(nums, k) - atMostK(nums, k - 1)