class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res=1
        N=len(s)
        
        for fences in range(1<<(N-1)):
            if bin(fences).count('1') < res: continue
            
            S=set()
            curr=s[0]
            unique=True
            
            for bit in range(N-1):
                if (fences>>bit)&1:
                    if curr in S:
                        unique=False
                        break

                    S.add(curr)
                    curr=''
                
                curr+=s[bit + 1]
            
            if curr in S: continue
            
            if unique: res=max(res,len(S)+1)


        return res