class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i=j=0
        while j<len(nums):
            if nums[j]==0: k-=1
            if k<0:
                if nums[i]==0:
                    k+=1
                i+=1
            j+=1
        
        
        return j-i
    # def longestOnes(self, A, K):
    #     i = 0
    #     for j in range(len(A)):
    #         K -= 1 - A[j]
    #         if K < 0:
    #             K += 1 - A[i]
    #             i += 1
    #     return j - i + 1
    # def longestOnes(self, nums: List[int], k: int) -> int:
    #     i=j=0
    #     while j<len(nums):
    #         if nums[j]==0: k-=1
    #         if k<0 and nums[i:=i+1]==0:
    #             k+=1

    #         j+=1


    #     return j-i