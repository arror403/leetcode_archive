class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        t=[]
        res=[]
        x=0
        j=0
        for i in s:
            if i.isalpha():
                t.append(i)

        t.reverse()

        # while x!=(len(s)-1):
        for _ in range(len(s)):
            if s[x].isalpha():
                res.append(t[j])
                j+=1
            else:
                res.append(s[x])
            x+=1


        return ''.join(res)