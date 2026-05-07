class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        m=sum(nums)/len(nums)
        if m<0: m=0

        for i in range(int(m)+1, 102):
            if i not in set(nums):
                return i