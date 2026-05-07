class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        def countLess(arr, v):
            res=0
            j=len(arr)-1
            for i in range(j+1):
                while(i<j and arr[i]+arr[j]>v): j-=1
                res+=max(0, j-i)

            return res

        nums.sort()


        return countLess(nums, upper)-countLess(nums, lower-1)