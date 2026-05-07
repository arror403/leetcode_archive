class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # return len([i for i in list(itertools.combinations(nums,2)) if i[0]==i[1]])

        # Count the occurrences of each element in nums
        # counter = Counter(nums)

        # Calculate the number of combinations where both elements are the same
        return sum(count * (count - 1) // 2 for count in Counter(nums).values())