class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res=0

        for a in arr1:
            f=1
            for b in arr2:
                if abs(a-b)<=d:
                    f=0
                    break
            
            if f: res+=1


        return res