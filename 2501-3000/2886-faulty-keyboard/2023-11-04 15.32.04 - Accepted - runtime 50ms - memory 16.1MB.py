class Solution:
    def finalString(self, s: str) -> str:
        res=[]
        for i in list(s):
            if i=='i': res.reverse()
            else: res.append(i)

        return ''.join(res)