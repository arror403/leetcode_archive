class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=['']
        for c in s:
            if c=='(':
                stack.append('')
            elif c==')':
                reversed_str=stack.pop()[::-1]
                stack[-1]+=reversed_str
            else:
                stack[-1]+=c
        return stack[0]


        # a,b=[],[]
        # t=list(s)

        # for i,c in enumerate(s):
        #     if c=="(": a.append(i)
        #     elif c==")": b.append(i)

        # m=list(zip(a,reversed(b)))

        # for a,b in reversed(m): t[a:b]=t[b:a:-1]


        # return ''.join([x for x in t if x not in ["(",")"]])

        # For reverse a certain range of elements:
        # a[2:6] = a[2:6][::-1]
        # This also can be achieved much faster
        # a[2:6] = a[5:1:-1]