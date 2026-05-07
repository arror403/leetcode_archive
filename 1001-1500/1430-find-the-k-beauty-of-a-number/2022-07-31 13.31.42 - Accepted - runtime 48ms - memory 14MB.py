class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num=str(num)
        m,t=[],0
        for i in range(len(num)-k+1):
            m.append(int(num[i:i+k]))
            
        num=int(num)
        
        for i in m:
            if i==0: continue
            elif num%i==0:
                t+=1
                
        return t