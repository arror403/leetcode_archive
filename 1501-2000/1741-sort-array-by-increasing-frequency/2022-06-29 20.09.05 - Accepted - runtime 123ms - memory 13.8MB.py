class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        b=[]
        output=[]
        nums.sort()
        nums.reverse()
        for i in nums:
            b.append(nums.count(i))
            
        for j in range(1,len(b)+1):
            for i in range(len(b)):
                if b[i] == j:
                    output.append(nums[i])
                        
        return output
                