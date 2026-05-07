class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.nums1_count = Counter(nums1)
        self.nums2_count = Counter(nums2)
        

    def add(self, index: int, val: int) -> None:
        v = self.nums2[index]
        self.nums2_count[v] -= 1
        self.nums2_count[v + val] += 1
        self.nums2[index] = v + val
    

    def count(self, tot: int) -> int:
        result = 0
        for v in self.nums1_count:
            val_needed = tot - v
            if val_needed in self.nums2_count:
                result += self.nums1_count[v]*self.nums2_count[val_needed]

        return result