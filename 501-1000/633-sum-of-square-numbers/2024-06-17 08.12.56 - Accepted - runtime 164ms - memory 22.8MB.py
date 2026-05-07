class Solution:
    def judgeSquareSum(self, n: int) -> bool:
        if n in [0,1]: return True

        d=defaultdict(int)

        for i in range(n):
            if (x:=i**2)>n: break

            d[x]=1

            if (n-x) in d: return True


        return False