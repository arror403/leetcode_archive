class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [j for i in nums for j in list(map(int,str(i)))]