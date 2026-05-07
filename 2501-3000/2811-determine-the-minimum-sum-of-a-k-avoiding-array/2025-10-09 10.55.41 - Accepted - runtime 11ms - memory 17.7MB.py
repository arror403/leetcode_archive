class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        p = [i for i in range(k//2 + 1, k)]
        res = 0
        x = 0
        # print(p)
        while n:
            x+=1
            if x in p:
                continue
            else:
                res+=x
                n-=1


        return res