class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        tmp=''
        x=0
        
        for i in range(len(s)):
            if s[i]!=' ':
                tmp+=s[i]
            elif s[i]==' ':
                tmp+=' '
                x+=1
            
            if x==k:
                tmp=tmp[:-1]
                break
                
        return tmp
        