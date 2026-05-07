class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        return any(2*v in (d:=Counter(arr)) and v!=0 for v in arr) or d[0]>1