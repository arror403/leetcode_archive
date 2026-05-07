class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums=deque(sorted(nums))
        return min([(nums.pop()+nums.popleft())/2 for _ in range(len(nums)//2)])