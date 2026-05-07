class Solution:
    def minOperations(self, n: int) -> int:
        m,res=[],0
        for i in range(n): m.append(2*i+1)
        # print(m)
        
        if n%2==0:
            for i in range(n//2): res+=m[i]
        else:
            for i in range(n//2): res+=(m[n//2]-m[i])
        
        return res