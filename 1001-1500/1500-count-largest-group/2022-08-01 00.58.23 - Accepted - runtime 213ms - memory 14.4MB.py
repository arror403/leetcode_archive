class Solution:
    def countLargestGroup(self, n: int) -> int:
        m,res,s=[],[],0
        for i in range(1,n+1):
            if sum(self.int_to_list(i))>s:
                s=sum(self.int_to_list(i))
                
        for i in range(s): m.append([0])
        
        if 9>=n>=0: return n
        else:
            for i in range(1,n+1):
                m[sum(self.int_to_list(i))-1].append(i)
            # print(m)
            for i in m:
                res.append(len(i))
        
            return res.count(max(res))
    
    
    def int_to_list(self,x):
        return list(map(int,str(x)))