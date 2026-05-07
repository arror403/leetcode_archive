class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0  # pointer for popped array
        for num in pushed:
            stack.append(num)  # push element to stack
            while stack and i < len(popped) and stack[-1] == popped[i]:
                stack.pop()  # pop elements from stack if they match with popped array
                i += 1  # move pointer in popped array
        return i == len(popped)  # return True if all elements in popped array are popped from stack
