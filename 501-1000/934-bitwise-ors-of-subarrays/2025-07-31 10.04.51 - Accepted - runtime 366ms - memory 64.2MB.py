class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res=[]
        l=0

        for v in arr:
            r = len(res)
            res.append(v)

            for i in range(l, r):
                if (res[-1] != (res[i] | v)):
                    res.append(res[i] | v)

            l = r


        return len(set(res))