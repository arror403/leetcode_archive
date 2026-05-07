class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d=Counter(arr)

        if d[0]>1: 
            return True
        else:
            del d[0]

        return bool(d.keys()&set(2*v for v in d.keys()))