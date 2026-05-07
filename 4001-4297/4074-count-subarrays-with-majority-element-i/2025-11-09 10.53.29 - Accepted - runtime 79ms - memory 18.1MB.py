class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        L = len(nums)
        
        # 1. Reframe the problem with scores (+1 for target, -1 for other)
        # and create the prefix sum array.
        # A subarray is a majority subarray if sum of scores > 0.
        # sum(scores[j:i+1]) > 0  =>  prefix[i+1] - prefix[j] > 0  =>  prefix[i+1] > prefix[j]
        # We need to count pairs (j, i) where j < i and prefix[j] < prefix[i].
        # (Using i and j for indices in the prefix sum array).
        
        prefix_sums = [0] * (L + 1)
        current_sum = 0
        for i in range(L):
            if nums[i] == target:
                current_sum += 1
            else:
                current_sum -= 1
            prefix_sums[i+1] = current_sum

        # 2. Count non-inversions using a modified merge sort.
        # This counts pairs (i, j) with i < j and arr[i] < arr[j].
        
        # We define the merge sort and count logic as a helper function.
        # It sorts the array `arr` and returns the count of non-inversions.
        def merge_sort_and_count(arr, low, high):
            if low >= high:
                return 0

            mid = (low + high) // 2
            
            # Recursively count in left and right halves
            count = merge_sort_and_count(arr, low, mid)
            count += merge_sort_and_count(arr, mid + 1, high)

            # Count pairs where one element is in the left half and the other is in the right
            l, r = low, mid + 1
            while l <= mid and r <= high:
                if arr[l] < arr[r]:
                    # If arr[l] < arr[r], then arr[l] is also smaller than all
                    # elements from arr[r] to arr[high].
                    # There are (high - r + 1) such elements.
                    count += (high - r + 1)
                    l += 1
                else:
                    # arr[l] >= arr[r], so this arr[r] doesn't form a valid pair with arr[l].
                    # Move to the next element in the right half to find a smaller one.
                    r += 1
            
            # Merge the two halves (standard merge sort procedure)
            # This is crucial to ensure the subarrays passed to the next level are sorted.
            arr[low:high+1] = sorted(arr[low:high+1])
            
            return count

        return merge_sort_and_count(prefix_sums, 0, L)