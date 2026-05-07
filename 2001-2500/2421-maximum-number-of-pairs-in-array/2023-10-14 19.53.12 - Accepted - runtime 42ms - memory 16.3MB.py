class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        return [sum(x) for x in zip(*[[i//2,i%2] for i in Counter(nums).values()])]

        