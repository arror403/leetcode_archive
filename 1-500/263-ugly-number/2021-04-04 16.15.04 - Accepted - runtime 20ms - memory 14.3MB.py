class Solution:
    def isUgly(self, n: int) -> bool:
        f=1
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n<0:
            return 0
        else:
            while n!=1:
                if n%2==0: n=int(n/2)
                elif n%3==0: n=int(n/3)
                elif n%5==0: n=int(n/5)
                else: 
                    f=0
                    break

            if(f): return 1
            else: return 0
        # return 0