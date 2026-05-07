class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        n1=t.count('1')
        n0=len(t)-n1
        r=0

        for c in s:
            if n0==0 or n1==0: break
            if c=='1':
                n0-=1
            elif c=='0':
                n1-=1
            r+=1

        x=(0 if n0 else 1)
        
        return '1'*r + ''.join([str(int(c)^x) for c in s[r:]])