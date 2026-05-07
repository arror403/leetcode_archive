class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # i=k=res=0
        # m=sorted(arr)

        # while i!=k:
        #     if m[i:k+1]==[v for v in range(k)]:
        #         k+=1
        #     else:
        #         i=k
        #         res+=1
            

        # return res

        chunks = 0
        max_so_far = 0
        
        for i in range(len(arr)):
            max_so_far = max(max_so_far, arr[i])
            # If the maximum number seen so far equals the current index,
            # we can make a valid chunk
            if max_so_far == i:
                chunks += 1
                
        return chunks