class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return 1
        else:
        
            tmp=self.fun3(num)
            tmp=self.fun3(tmp)


            if tmp == num:
                return 1
            else:
                return 0
        

    def fun(self, n: int) -> List[int]:
        return list(map(int,str(n)))
    
    
    def fun2(self, n: List[int]) -> List[int]:
        while n[0]==0:
            del n[0]
        return n
    
    
    def fun3(self, n:int) -> int:
        n=self.fun(n)
        n.reverse()
        n=self.fun2(n)
        n = [str(i) for i in n]
        n=''.join(n)
        n=int(n)
        return n