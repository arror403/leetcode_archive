class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count=0
        prefix_sum=[0]
        for i in nums:
            prefix_sum.append(prefix_sum[-1]+i)

        freq={}
        for i in range(len(prefix_sum)):
            if (prefix_sum[i]-goal) in freq:
                count+=freq[prefix_sum[i]-goal]
            if prefix_sum[i] in freq:
                freq[prefix_sum[i]]+=1
            else:
                freq[prefix_sum[i]]=1

        return count

        # n = len(nums)
        # count = 0
        # sum_so_far = 0
        # prefix_sum = {0: 1}  # Initialize with 0 as the starting sum

        # for num in nums:
        #     sum_so_far += num
        #     if sum_so_far - goal in prefix_sum:
        #         count += prefix_sum[sum_so_far - goal]
        #     prefix_sum[sum_so_far] = prefix_sum.get(sum_so_far, 0) + 1

        # return count