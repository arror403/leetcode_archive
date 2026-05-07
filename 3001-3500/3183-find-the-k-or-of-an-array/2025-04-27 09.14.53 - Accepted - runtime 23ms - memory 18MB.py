class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        b=[bin(v)[2:] for v in nums]
        L=max(b, key=len)
        L=len(L)
        b=[v.zfill(L) for v in b]
        res=""

        for i in range(L):
            c=0
            for j in range(len(nums)):
                c+=(b[j][i]=="1")

            res+="1" if c>=k else "0"


        return int(res, 2)