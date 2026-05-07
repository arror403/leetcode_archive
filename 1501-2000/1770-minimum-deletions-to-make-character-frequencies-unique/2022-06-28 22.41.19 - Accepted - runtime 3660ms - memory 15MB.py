class Solution:
    def minDeletions(self, s: str) -> int:
        t=0
        b=[]
        c=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
        for i in range(26):
            b.append(0)
        
        for i in range(len(s)):
            for j in range(26):
                if s[i]==c[j]:
                    b[j]+=1
                    break
        b.sort()

        while 1:
            b=self.fun(b)
            for i in range(len(b)):
                if b.count(b[i])>=2:
                    b[i]-=1
                    t+=1
            if self.fun2(b):
                break
                
        return t
                    
        
        
    def fun(self, num: List[int]) -> List[int]:
        while 1:
            if num[0]==0:
                del num[0]
            else:
                break   
        return num
    
    
    
    def fun2(self,num: List[int]) -> bool:
        f=1
        for i in range(len(num)-1):
            if num[i] < num[i+1]:
                continue
            else:
                f=0
                break
        return f
            
        
        