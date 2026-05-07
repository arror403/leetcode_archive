class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        m=[list(j) for i in range(1,len(nums)+1) for j in itertools.combinations(nums,i)]
        # print(m)
        c,res=-inf,0
        for i in m:
            tmp=reduce(self.fun_or,i)
            # print(tmp)
            if tmp>c:
                c=tmp
                
        for i in m:
            if reduce(self.fun_or,i)==c:
                res+=1
        
            
        return res
    
    
    
    def fun_or(self, a, b):
        return a | b