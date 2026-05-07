class Solution:
    def isNStraightHand(self, nums: List[int], k: int) -> bool:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        unique_nums = sorted(set(nums))
        for num in unique_nums:
            if count[num] > 0:
                for i in range(1, k):
                    next_num = num + i
                    if next_num not in count or count[next_num] < count[num]:
                        return False
                    count[next_num] -= count[num]

        return True