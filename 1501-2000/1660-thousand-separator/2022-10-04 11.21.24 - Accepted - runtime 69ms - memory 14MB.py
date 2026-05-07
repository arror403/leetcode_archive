class Solution:
    def thousandSeparator(self, n: int) -> str:
        if len(str(n))<=3: return str(n)
        n=str(n)
        n=n[::-1]
        x=0
        res=''
        for i in n:
            res+=i
            x+=1
            if x%3==0: res+='.'
        res=res[::-1]
        if res[0]=='.': return res[1:]

        return res