class Solution:
    def judgeSquareSum(self, n: int) -> bool:
        if n in [0,1]: return True

        d=set()
        
        for i in range(int(n**0.5)+1):
            if (square:=i**2)>n: break

            d.add(square)

            if (n-square) in d: return True


        return False