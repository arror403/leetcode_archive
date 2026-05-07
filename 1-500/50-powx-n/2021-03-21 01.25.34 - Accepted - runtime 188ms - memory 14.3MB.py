class Solution:
    def myPow(self, x: float, n: int) -> float:
        tmp=1.0
        if x==1:return tmp
        elif x==-1:
            if n%2==1: return -1
            else: return 1 
        else:
            if n>0:
                for i in range(0,n):
                    tmp*=x
                    if tmp==0: break

                return tmp  
            elif n<0:
                for i in range(0,(-1)*n):
                    tmp*=x
                    if tmp>100000000: 
                        tmp=0
                        break
                if tmp!=0:        
                    tmp=1/tmp
                return tmp  

            elif n==0:
                return tmp