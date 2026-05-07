class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        first = self.binarySearch(nums, 0, len(nums)-1, target, True)
        last = self.binarySearch(nums, 0, len(nums)-1, target, False)
        
        return [first,last]

        
    def binarySearch(self, arr, l, r, x, searchFirst):
        result = -1
        while l <= r:
            mid = (l+r) // 2
            # Check if x is present at mid
            if arr[mid] == x:
                result = mid
                if searchFirst:
                    r = mid-1
                else:
                    l = mid+1
            # If x is greater, ignore left half
            elif arr[mid] < x:
                l = mid+1
            # If x is smaller, ignore right half
            else:
                r = mid-1
        # If we reach here, then the element was not present
        return result