class Solution:
    def sumBase(self, n: int, k: int) -> int:
            s=[]
            while n>=k:
                s.append(n%k)
                n=int(n/k)
            s.append(n)
            
            return sum(s)
