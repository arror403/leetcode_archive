class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        f=0
        if (0 in arr): arr.remove(0)
        arr.sort()
        for i in arr:
            if ((2*i) in arr):
                f=1
                break
        
        # print (arr)
                
        return f