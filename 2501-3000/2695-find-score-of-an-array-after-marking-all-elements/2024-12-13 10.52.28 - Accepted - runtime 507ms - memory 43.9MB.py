class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap=[]
        seen=set()
        res=0
        for i,v in enumerate(nums): heappush(heap, (v,i))
        
        while heap:
            # Get the smallest unmarked element
            val, idx = heappop(heap)

            # If this index is already marked, continue
            if idx in seen: continue

            res+=val
            seen.add(idx)
            seen.add(idx-1)
            seen.add(idx+1)
        

        return res