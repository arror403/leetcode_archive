class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d=defaultdict(int)

        for k,v in (nums1+nums2): d[k]+=v

        return sorted([[k,v] for k,v in d.items()],key=lambda x:x[0])