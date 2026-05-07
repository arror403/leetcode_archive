class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n,k=len(nums),len(set(nums))
        res=i=0
        count=defaultdict(int)

        for j in range(n):
            k-=(count[nums[j]]==0)
            count[nums[j]]+=1
            while k==0:
                count[nums[i]]-=1
                k+=(count[nums[i]]==0)
                i+=1

            res+=i
        

        return res