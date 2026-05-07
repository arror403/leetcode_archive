class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        t=[heights[i]-heights[i-1] for i in range(1,len(heights))]
        heap = []
        for i,v in enumerate(t):
            if v>0:
                if ladders>0:
                    heappush(heap, v)
                    ladders-=1
                elif heap and v>heap[0]:
                    bricks-=heappop(heap)
                    heappush(heap, v)
                else:
                    bricks-=v
                if bricks<0:
                    return i
        return len(heights)-1

        # t=[heights[i]-heights[i-1] for i in range(1,len(heights))]
        # res=0
        # for i,v in enumerate(t):
        #     if v<=0:
        #         res+=1
        #         continue

        #     if v<=bricks:
        #         res=(i+1)
        #         bricks-=v
        #     elif ladders>0:
        #         ladders-=1
        #     else:
        #         return res

        # return res