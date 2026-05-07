class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n=len(s)
        res=0
        st=[]

        for i in range(n):
            if s[i]=='(': st.append(i)
            else:
                if st:
                    if s[st[-1]]=='(': st.pop()
                    else: st.append(i)

                else: st.append(i)

        if not st: res=n
        else:
            a=n
            b=0
            while st:
                b=st.pop()
                res=max(res, a-b-1)
                a=b

            res=max(res, a)

        return res