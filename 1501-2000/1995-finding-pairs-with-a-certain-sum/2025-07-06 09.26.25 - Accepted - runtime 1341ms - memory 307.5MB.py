class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.t=nums2
        self.a=defaultdict(set)
        self.b=defaultdict(set)

        for i,v in enumerate(nums1):
            self.a[v].add(i)

        for i,v in enumerate(nums2):
            self.b[v].add(i)


    def add(self, index: int, val: int) -> None:
        k=self.t[index]
        self.b[k].remove(index)
        self.b[k+val].add(index)
        self.t[index]+=val


    def count(self, tot: int) -> int:
        return sum(len(self.a[k])*len(self.b[tot-k]) for k in self.a.keys())
        
        # return sum(len(self.a[i])*len(self.b[tot-i]) for i in range(tot))
            


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)