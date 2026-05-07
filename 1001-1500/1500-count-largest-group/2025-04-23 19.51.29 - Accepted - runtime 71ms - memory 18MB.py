class Solution:
    def countLargestGroup(self, n: int) -> int:
        def dsum(n): return 0 if n==0 else n%10+dsum(n//10)
        
        d,m=[0]*37,0

        for i in range(1,n+1):
            d[dsum(i)]+=1
            m=max(m, d[dsum(i)])


        return d.count(m)