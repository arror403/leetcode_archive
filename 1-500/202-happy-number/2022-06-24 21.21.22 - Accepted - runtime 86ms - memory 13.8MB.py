class Solution:
    def isHappy(self, n: int) -> bool:
        loop_time=0
        while 1:
            loop_time+=1
            sum=0
            t=self.intToList(n)
            for i in t:
                sum+=i**2
            if sum==1:
                return 1
                break
            else:
                n=sum
                if loop_time==10:
                    return 0
                    break

        
    def intToList(self,x:int) -> List[int]:
        return list(map(int, str(x)))