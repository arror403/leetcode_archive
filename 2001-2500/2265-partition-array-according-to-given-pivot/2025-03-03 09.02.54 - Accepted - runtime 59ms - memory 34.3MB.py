class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        low = same = high = 0

        for v in nums:      
            if v < pivot:
                low+=1
            elif v == pivot:
                same+=1

        res = [0]*len(nums)
        high = same + low
        same = low
        low = 0

        for v in nums:
            if v < pivot:
                res[low] = v
                low+=1
            
            elif v == pivot:
                res[same] = v
                same+=1
            
            else:
                res[high] = v
                high+=1


        return res