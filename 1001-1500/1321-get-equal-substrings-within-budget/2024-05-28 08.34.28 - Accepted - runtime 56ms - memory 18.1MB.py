class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        def max_subarray_len(nums, M):
            ##### function powered by Claude #####
            n = len(nums)
            max_len = 0
            curr_sum = 0
            start = 0

            for end in range(n):
                curr_sum += nums[end]

                while curr_sum > M:
                    curr_sum -= nums[start]
                    start += 1

                max_len = max(max_len, end - start + 1)

            return max_len


        L=len(s)
        d=[abs(ord(s[i])-ord(t[i])) for i in range(L)]


        return max_subarray_len(d,maxCost)