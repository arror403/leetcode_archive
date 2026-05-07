class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        L=len(nums)
        res=0
        
        for i in range(L):
            if L-i <= res: break

            s=[set(),set()]
            for j in range(i, L):
                s[nums[j]%2].add(nums[j])
                if len(s[0])==len(s[1]):
                    res=max(res, j-i+1)


        return res