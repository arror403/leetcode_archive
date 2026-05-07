class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        ##### improved by chatGPT #####

        L = len(nums)
        res = [0] * L
        p_idx, n_idx = 0, 1

        for num in nums:
            if num > 0:
                res[p_idx] = num
                p_idx += 2
            else:
                res[n_idx] = num
                n_idx += 2

        return res