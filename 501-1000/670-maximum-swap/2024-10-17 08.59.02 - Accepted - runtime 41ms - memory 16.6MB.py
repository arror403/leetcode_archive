class Solution:
    def maximumSwap(self, num: int) -> int:
        if 0<=num<=9: return num

        def to_list(x):
            return list(map(int,str(x)))
        def to_int(l):
            return int(''.join([str(x) for x in l]))

        
        res=[]
        
        if len(str(num))==2:
            res.append(num)
            num=to_list(num)
            num[0],num[1]=num[1],num[0]
            res.append(to_int(num))
            
            return max(res[0],res[1])
            
        res.append(num)
        num=to_list(num)
        
        for i in range(len(num)):
            for j in range(i+1,len(num)):
                num[i],num[j]=num[j],num[i]
                res.append(to_int(num))
                num[i],num[j]=num[j],num[i]
                
                
        return max(res)