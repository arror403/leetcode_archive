import random
# power by chatGPT
class Solution:
    def findKthLargest(self, nums, k):
        def partition(left, right, pivot_idx):
            pivot_value = nums[pivot_idx]
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            store_idx = left
            for i in range(left, right):
                if nums[i] > pivot_value:
                    nums[i], nums[store_idx] = nums[store_idx], nums[i]
                    store_idx += 1
            nums[right], nums[store_idx] = nums[store_idx], nums[right]
            return store_idx
        
        def quickselect(left, right, k_smallest):
            if left == right:
                return nums[left]
            
            pivot_idx = random.randint(left, right)
            pivot_idx = partition(left, right, pivot_idx)
            
            if k_smallest == pivot_idx:
                return nums[k_smallest]
            elif k_smallest < pivot_idx:
                return quickselect(left, pivot_idx - 1, k_smallest)
            else:
                return quickselect(pivot_idx + 1, right, k_smallest)
        
        return quickselect(0, len(nums) - 1, k - 1)