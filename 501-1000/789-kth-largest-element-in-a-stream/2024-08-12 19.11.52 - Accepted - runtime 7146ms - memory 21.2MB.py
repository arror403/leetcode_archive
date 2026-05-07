class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=-k
        self.nums=sorted(nums)

    def add(self, val: int) -> int:
        self.nums.append(val)
        return sorted(self.nums)[self.k]