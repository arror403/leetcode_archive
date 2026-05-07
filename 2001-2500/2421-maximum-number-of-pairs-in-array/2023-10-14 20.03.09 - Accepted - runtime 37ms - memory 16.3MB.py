class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        # return [sum(x) for x in zip(*[[i//2,i%2] for i in Counter(nums).values()])]
        return [sum(v//2 for v in Counter(nums).values()), sum(v%2 for v in Counter(nums).values())]