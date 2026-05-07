class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        c=i=0
        res=[]

        for j in range(len(s)):
            c+=(1 if s[j]=='1' else -1)
            if c==0:
                res.append('1'+self.makeLargestSpecial(s[i+1:j])+'0')
                i=j+1

        res.sort(reverse=True)


        return ''.join(res)