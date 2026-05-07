class Solution:
    def sumSubarrayMins(self, lst: List[int]) -> int:

        ##### power by chatGPT #####

        stack = []
        result = 0

        for i, num in enumerate(lst):
            while stack and num < lst[stack[-1]]:
                # Pop elements from the stack until the top is greater than the current element
                popped_index = stack.pop()
                result += lst[popped_index] * (i - popped_index) * (popped_index - (stack[-1] if stack else -1))

            stack.append(i)

        # Process any remaining elements in the stack
        while stack:
            popped_index = stack.pop()
            result += lst[popped_index] * (len(lst) - popped_index) * (popped_index - (stack[-1] if stack else -1))

        return result%(10**9+7)