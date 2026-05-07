class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        b=[]
        index=n
        for i in range(0,n):
            b.append(nums[i])
            b.append(nums[index])
            index+=1
            
        return b