class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        d={}
        for v in set(nums): d[v]=int(bin(v)[2:][::-1], 2)
            
        return sorted(nums, key=lambda x:(d[x],x))