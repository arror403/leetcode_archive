class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        def is_Arithmetic(m):
            if len(m)<2: return False

            diff=m[1]-m[0]
            for i in range(len(m)-1):
                if (m[i+1]-m[i]) != diff:
                    return False
            return True


        return [is_Arithmetic(sorted(nums[l[i]:r[i]+1])) for i in range(len(l))]