class Solution:
    ##### improved by Claude #####
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        pairs={}
        
        # Step 1: Find matching pairs of parentheses
        for i,c in enumerate(s):
            if c=='(':
                stack.append(i)
            elif c==')':
                j=stack.pop()
                pairs[i],pairs[j]=j,i
        
        # Step 2: Traverse the string, flipping direction at each parenthesis
        res = []
        direction=1
        i=0
        
        while i<len(s):
            if s[i] in '()':
                i=pairs[i]
                direction*=-1
            else:
                res.append(s[i])

            i+=direction
        
        return ''.join(res)