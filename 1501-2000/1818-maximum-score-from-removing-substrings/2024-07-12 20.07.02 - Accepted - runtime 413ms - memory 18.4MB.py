class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack=[]
        res=0
        p,q='a','b'

        if y>x: 
            x,y=y,x
            p,q=q,p

        for c in s:
            if stack and [stack[-1],c]==[p,q]:
                stack.pop()
                res+=x
            else:
                stack.append(c)

        s=''.join(stack)
        stack=[]

        for c in s:
            if stack and [stack[-1],c]==[q,p]:
                stack.pop()
                res+=y
            else:
                stack.append(c)


        return res