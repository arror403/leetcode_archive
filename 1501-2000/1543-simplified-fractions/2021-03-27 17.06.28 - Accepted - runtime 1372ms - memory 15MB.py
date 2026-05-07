class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        b=[]
        a=''
        for i in range(1,n+1):
            for j in range(i,n+1):
                if i==j: continue
                else:
                    # print (f"{i}/{j}")
                    tmp=self.computeGCD(i,j)
                    p=int(i/tmp)
                    q=int(j/tmp)
                    a=(f"{p}/{q}")
                    # print (a)
                    if not(a in b): b.append(a)
                        
        
        return b
        
    def computeGCD(self, x : int, y : int) -> int:
        while(y):
            x , y = y , x%y
        return x