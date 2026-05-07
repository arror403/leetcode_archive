class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        max_element = 1

        for i in range(1, len(arr)):
            max_element = min(arr[i], max_element+1)

        return max_element