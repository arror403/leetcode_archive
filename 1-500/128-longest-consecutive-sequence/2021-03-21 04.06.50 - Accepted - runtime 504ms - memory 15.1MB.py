class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x=[]
        b=[]
        sum=0
        index=0
        nums.sort()
        
        for i in nums: 
            if i not in x: 
                x.append(i) 
        # print (x)
        while 1:
            if index<len(x)-1:
                if x[index]==x[index+1]-1:
                    sum+=1
                    index+=1
                else:
                    index+=1
                    b.append(sum+1)
                    sum=0
            else: break
        b.append(sum+1)
        # print (b)
        
        if len(x)==0: return 0
        else: return max(b)