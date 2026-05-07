class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        res = [list(y) for x, y in groupby(arr)]
        r=-inf
        len_arr=len(arr)
        for i in res:
            if (len(i)/len_arr)>0.25:
                return i[0]