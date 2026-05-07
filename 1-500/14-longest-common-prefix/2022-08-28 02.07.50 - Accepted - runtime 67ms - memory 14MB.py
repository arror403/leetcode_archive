class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=''
        strs=sorted(strs,key=len)
        mlen=len(strs[0])
        for i in range(mlen):
            tmp=strs[0][i]
            for j in strs:
                f=True
                if j[i]==tmp: 
                    continue
                else:
                    f=False
                    break
            if f: res+=tmp
            else: break
                
        # print(strs,mlen)
        
        return res