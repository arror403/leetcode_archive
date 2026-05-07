class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd=[]
        even=[]
        res=[]
        for i in range(len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])

        odd.sort()
        odd.reverse()
        even.sort()

        for i in range(min(len(odd),len(even))):
            res.append(even[i])
            res.append(odd[i])

        if len(odd)>len(even):
            res.append(odd[-1])
        elif len(odd)<len(even):
            res.append(even[-1])

        return res