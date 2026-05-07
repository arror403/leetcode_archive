class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s={i:False for i in range(1,k+1)}
        res=0
        for i in reversed(nums):
            s[i]=True
            res+=1
            if all(s.values()): break

        return res