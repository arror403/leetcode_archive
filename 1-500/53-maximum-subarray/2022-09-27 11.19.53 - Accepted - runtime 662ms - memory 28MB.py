class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def maxSubArraySum(a, size):
            max_so_far = -inf
            max_ending_here = 0
            start = 0
            end = 0
            s = 0
            
            for i in range(0, size):

                max_ending_here += a[i]

                if max_so_far < max_ending_here:
                    max_so_far = max_ending_here
                    start = s
                    end = i

                if max_ending_here < 0:
                    max_ending_here = 0
                    s = i+1
            return max_so_far
            # print("Maximum contiguous sum is %d" % (max_so_far))
            # print("Starting Index %d" % (start))
            # print("Ending Index %d" % (end))
            
        return maxSubArraySum(nums,len(nums))