class Solution:
    ##### improved by Claude #####
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = deque()
        ans = deque()
        k = 1
        
        for i, v in enumerate(nums):
            if v > 0:
                seen.appendleft(v)
            elif v == -1:
                if k <= len(seen):
                    ans.append(seen[k-1])
                else:
                    ans.append(-1)
                if i < len(nums) - 1 and nums[i+1] != -1:
                    k = 1
                else:
                    k += 1
        
        return list(ans)