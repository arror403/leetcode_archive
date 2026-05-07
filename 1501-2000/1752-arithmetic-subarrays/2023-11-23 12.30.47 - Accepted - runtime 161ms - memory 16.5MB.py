class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        def is_Arithmetic(subarray):
            if len(subarray)<2: return False

            min_val, max_val = min(subarray), max(subarray)
            length = len(subarray)
            
            if (max_val - min_val) % (length - 1) != 0:
                return False

            common_diff = (max_val - min_val) // (length - 1)

            return all(min_val + i * common_diff in subarray for i in range(length))


        return [is_Arithmetic(nums[l[i]:r[i]+1]) for i in range(len(l))]