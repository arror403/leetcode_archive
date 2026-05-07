class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        def helper(left, right, max_deque, min_deque, max_len):
            if right == len(nums): return max_len

            # Maintain the max deque
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
                
            max_deque.append(right)

            # Maintain the min deque
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)

            # If the current window is invalid, move the left pointer
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()

            # Calculate the current window length
            current_len = right - left + 1
            max_len = max(max_len, current_len)

            # Recur for the next element
            return helper(left, right + 1, max_deque, min_deque, max_len)

        # Initialize deques and call the helper function
        return helper(0, 0, deque(), deque(), 0)