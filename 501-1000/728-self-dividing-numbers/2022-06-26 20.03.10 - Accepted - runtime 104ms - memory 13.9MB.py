class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        b=[]
        for i in range(left,right+1):
            if self.fun(i):
                b.append(i)
            
        return b
            
            
    def fun(self, n:int) -> bool:
        f=1
        x=list(map(int,str(n)))
        x=list(dict.fromkeys(x))
        for i in x:
            if i==0 or (n%i)!=0:
                f=0
                break
        return f