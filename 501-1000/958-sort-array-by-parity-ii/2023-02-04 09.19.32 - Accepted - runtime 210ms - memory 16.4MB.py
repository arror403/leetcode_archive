class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd=[]
        even=[]
        res=[]
        for i in nums:
            if i%2==0: even.append(i)
            else: odd.append(i)
        e,o=0,0
        for i in range(len(nums)):
            if i%2==0: 
                res.append(even[e])
                e+=1
            else:
                res.append(odd[o])
                o+=1
        return res