class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        ##### power by chatGPT #####

        stack=[]
        res=0

        for i,v in enumerate(arr):
            while stack and v<arr[stack[-1]]:
                # Pop elements from the stack until the top is greater than the current element
                popped_index=stack.pop()
                res+=arr[popped_index]*(i-popped_index)*(popped_index-(stack[-1] if stack else -1))
            stack.append(i)

        # Process any remaining elements in the stack
        while stack:
            popped_index=stack.pop()
            res+=arr[popped_index]*(len(arr)-popped_index)*(popped_index-(stack[-1] if stack else -1))


        return res%(10**9+7)