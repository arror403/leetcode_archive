class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
 
        def process_string(s: str) -> str:
            stack = []
            for c in s:
                if c != '#':
                    stack.append(c)
                elif stack:
                    stack.pop()
            return stack
        
        return process_string(s) == process_string(t)