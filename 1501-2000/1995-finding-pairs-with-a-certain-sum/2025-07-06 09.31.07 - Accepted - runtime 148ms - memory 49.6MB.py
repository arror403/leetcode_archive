class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.nums1_indices = defaultdict(set)
        self.nums2_count = defaultdict(int)
        
        for i, v in enumerate(nums1): self.nums1_indices[v].add(i)
        
        for v in nums2: self.nums2_count[v] += 1

    
    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = old_val + val
        
        # Update count mapping
        self.nums2_count[old_val] -= 1
        if self.nums2_count[old_val] == 0:
            del self.nums2_count[old_val]
        self.nums2_count[new_val] += 1
        
        # Update actual array
        self.nums2[index] = new_val
    

    def count(self, tot: int) -> int:
        result = 0

        for val1 in self.nums1_indices:
            val2_needed = tot - val1
            if val2_needed in self.nums2_count:
                result += len(self.nums1_indices[val1]) * self.nums2_count[val2_needed]


        return result