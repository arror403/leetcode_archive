class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        left, right = 0, n - 1

        # If the target is greater than the last letter or smaller than the first letter,
        # the result should be the first letter in the list.
        if target >= letters[n - 1] or target < letters[0]:
            return letters[0]

        while left <= right:
            mid = left + (right - left) // 2

            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        # The smallest letter greater than the target will be at index "left".
        return letters[left]