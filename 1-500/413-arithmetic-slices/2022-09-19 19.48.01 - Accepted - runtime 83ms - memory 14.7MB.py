class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        r,s=[],0
        
        for i in range(1,len(nums)): r.append(nums[i]-nums[i-1])
            
        res = [list(y) for x,y in groupby(r)]
        # print(res)
        
        for i in res:
            tmp=len(i)
            if tmp>=2:
                s+=int(tmp*(tmp-1)/2)
        
        return s