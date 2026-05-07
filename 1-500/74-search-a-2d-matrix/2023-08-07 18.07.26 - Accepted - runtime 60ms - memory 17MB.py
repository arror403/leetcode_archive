class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # return target in list(chain.from_iterable(matrix))
        return self.binary_search(list(chain.from_iterable(matrix)),target)

    def binary_search(self, arr, target):
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False