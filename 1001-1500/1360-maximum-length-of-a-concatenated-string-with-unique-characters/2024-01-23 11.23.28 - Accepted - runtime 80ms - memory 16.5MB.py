class Solution:
    def maxLength(self, arr: List[str]) -> int:

        ##### power by chatGPT #####

        def is_unique(combination):
            return len(combination) == len(set(combination))

        def backtrack(start, current):
            nonlocal max_length
            max_length = max(max_length, len(current))

            for i in range(start, len(arr)):
                if is_unique(current + arr[i]):
                    backtrack(i + 1, current + arr[i])

        max_length = 0
        backtrack(0, "")
        return max_length