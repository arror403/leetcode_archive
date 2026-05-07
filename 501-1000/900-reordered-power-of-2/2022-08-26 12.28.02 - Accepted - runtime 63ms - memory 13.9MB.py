class Solution:
    def reorderedPowerOf2(self, x: int) -> bool:
        res,n=[],1
        
        while n<=(10**9):
            d={}
            tmp=list(map(int,str(n)))
            for i in list(dict.fromkeys(tmp)): d[i]=0
            for i in tmp: d[i]+=1
            res.append(d)
            n*=2
        
        # print(res)
        
        d={}    
        tmp=list(map(int,str(x)))
        for i in list(dict.fromkeys(tmp)): d[i]=0
        for i in tmp: d[i]+=1
            
        # print(d)
            
        for i in res: 
            if i==d:
                return True
            
        return False