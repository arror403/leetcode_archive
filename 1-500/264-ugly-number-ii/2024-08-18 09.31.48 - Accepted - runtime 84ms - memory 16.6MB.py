class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly=[1]*n
        i2=i3=i5=0
        
        for i in range(1,n):
            u2, u3, u5 = 2*ugly[i2], 3*ugly[i3], 5*ugly[i5]
            ugly[i]=min(u2,u3,u5)
            
            if ugly[i]==u2: i2+=1
            if ugly[i]==u3: i3+=1
            if ugly[i]==u5: i5+=1
        
        
        return ugly[-1]