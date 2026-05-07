class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        for i in range(int(math.sqrt(num+2)),0,-1):
            if (num+1)%i==0: 
                return [(num+1)//i,i]
            if (num+2)%i==0:
                return [(num+2)//i,i]
