class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        stack = []
        n = len(A)
        
        # Build a decreasing stack of indices
        for i in range(n):
            if not stack or A[stack[-1]] > A[i]:
                stack.append(i)
        
        max_width = 0
        
        # Iterate from right to left to find the maximum width
        for i in range(n - 1, -1, -1):
            while stack and A[stack[-1]] <= A[i]:
                max_width = max(max_width, i - stack.pop())
        
        return max_width