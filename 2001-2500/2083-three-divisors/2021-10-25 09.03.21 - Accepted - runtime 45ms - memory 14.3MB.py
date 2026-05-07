class Solution:
    def isThree(self, n: int) -> bool:
        re=0
        for i in range(1,n+1):
            # print(i)
            if (n%i)==0:
                re+=1
            if re>3:
                break
                
        if re==3:
            return 1
        else:
            return 0