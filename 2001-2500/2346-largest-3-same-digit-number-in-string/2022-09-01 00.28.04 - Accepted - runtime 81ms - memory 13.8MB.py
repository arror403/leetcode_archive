class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res=[]
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                res.append(num[i])
                
        if len(res)==0: return ""        
                
        r=max(res)
        
        return str(r)+str(r)+str(r)