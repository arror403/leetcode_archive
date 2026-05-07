class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num==0: return True

        def f(n):
            n=list(map(int,str(n)))[::-1]
            while n[0]==0: del n[0]
            return int(''.join([str(i) for i in n]))


        return f(f(num))==num