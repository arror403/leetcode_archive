class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        def count_pairs(mid):
            count=l=0
            for r in range(1,len(nums)):
                while (nums[r]-nums[l])>mid:
                    l+=1
                count+=(r-l)

            return count
        
        low, high = 0, nums[-1]-nums[0]
        while low<high:
            mid=(low+high)//2
            if count_pairs(mid)<k:
                low=mid+1
            else:
                high=mid
        

        return low