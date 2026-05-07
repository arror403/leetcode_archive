class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        ans=1
        for i in range(0,len(arr)):
            if target[i]!=arr[i]:
                ans=0
                break
                
        return ans