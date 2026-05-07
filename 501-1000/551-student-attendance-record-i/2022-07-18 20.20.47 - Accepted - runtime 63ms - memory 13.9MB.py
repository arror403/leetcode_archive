class Solution:
    def checkRecord(self, s: str) -> bool:
        a,l,f=0,0,False
        
        for i in s: 
            if i=='A': a+=1
        
        for i in range(1,len(s)-1):
            if s[i-1]=='L' and s[i]=='L' and s[i+1]=='L':
                f=True
                break
                
        return 1 if a<2 and f==False else 0
            