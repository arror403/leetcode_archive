class Solution:
    
    ##### power by chatGPT #####

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums=list(map(lambda x:x%2,nums))
        print(nums)
        count = 0
        current_sum = 0
        sum_freq = {0: 1}  # Initialize with 0 to handle subarrays starting from index 0

        for num in nums:
            current_sum += num
            # If the complement (current_sum - k) exists in the hashmap, increment count
            count += sum_freq.get(current_sum - k, 0)
            # Increment the frequency of current_sum in the hashmap
            sum_freq[current_sum] = sum_freq.get(current_sum, 0) + 1

        return count