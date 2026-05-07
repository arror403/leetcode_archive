class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        f=0

        u=int(num**(0.5))

        for i in range(1,u+1):
            if (i*i)==num:
                f=1
                break

        if f :
            return 1
        else:
            return 0