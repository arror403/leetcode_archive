class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return chain.from_iterable([[v]*f for v,f in sorted(Counter(sorted(nums,reverse=True)).items(), key=lambda x:x[1])])