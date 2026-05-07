class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq=[(r[0], i, 0) for i,r in enumerate(nums)]
        heapify(pq)
        res=[-inf,inf]
        right=max(row[0] for row in nums)

        while pq:
            left,i,j=heappop(pq)

            if right-left<res[1]-res[0]: res=[left,right]
            if j+1==len(nums[i]): return res

            v=nums[i][j+1]
            right=max(right,v)
            heappush(pq, (v, i, j+1))