class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack,star_stack=[],[]

        for i,c in enumerate(s):
            if c=='(':
                open_stack.append(i)
            elif c=='*':
                star_stack.append(i)
            elif c==')':
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False

        while open_stack and star_stack:
            if open_stack[-1] < star_stack[-1]:
                open_stack.pop()
                star_stack.pop()
            else:
                break

        return len(open_stack)==0



        # s=list(s)
        # stack=[]

        # for i,c in enumerate(s):
        #     if c=='(' or c=='*':
        #         stack.append(i)
        #     elif c==')' or c=='*':
        #         if stack:
        #             stack.pop()
        #         else:
        #             return False

        # while stack:
        #     if s[stack.pop()]=='(':
        #         return False

        # return True
