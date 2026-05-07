class Solution:
    def findComplement(self, num: int) -> int:
        num=bin(num)[2:]
        res=[]
        for i in num:
            if i=='1': res.append(0)
            else: res.append(1)

        res=''.join([str(i) for i in res])

        return int(res,2)