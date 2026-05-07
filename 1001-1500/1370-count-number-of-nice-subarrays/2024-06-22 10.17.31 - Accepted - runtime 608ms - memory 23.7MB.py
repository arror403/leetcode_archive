class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums=list(map(lambda x:x%2, nums))
        res=0
        current_sum=0
        sum_freq={0:1}

        for v in nums:
            current_sum+=v
            # If the complement (current_sum - k) exists in the hashmap, increment count
            res+=sum_freq.get(current_sum-k, 0)
            # Increment the frequency of current_sum in the hashmap
            sum_freq[current_sum]=sum_freq.get(current_sum, 0)+1


        return res