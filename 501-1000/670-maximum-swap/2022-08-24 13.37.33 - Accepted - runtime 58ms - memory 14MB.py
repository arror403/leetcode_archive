class Solution:
    def maximumSwap(self, num: int) -> int:
        if 0<=num<=9: return num
        
        res=[]
        
        if len(str(num))==2:
            res.append(num)
            num=list(map(int,str(num)))
            num[0],num[1]=num[1],num[0]
            res.append(int(''.join([str(x) for x in num])))
            print(res)
            return res[0] if res[0]>res[1] else res[1]
            
        res.append(num)
        num=list(map(int,str(num)))
        
        
        for i in range(len(num)):
            for j in range(i+1,len(num)):
                num[i],num[j]=num[j],num[i]
                res.append(int(''.join([str(x) for x in num])))
                num[i],num[j]=num[j],num[i]
                
        print(res)
                
        return max(res)