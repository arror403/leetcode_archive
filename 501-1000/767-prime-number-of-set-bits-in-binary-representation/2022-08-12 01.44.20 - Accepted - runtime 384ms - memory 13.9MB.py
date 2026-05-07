class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res=0
        for i in range(left,right+1):
            if self.is_prime(bin(i)[2:].count('1')):
                # print(bin(i)[2:] , bin(i)[2:].count('1'))
                res+=1
                
        return res
            
            
            
            

    def is_prime(self, n):
        if n==1: return False
        for i in range(2,int(math.sqrt(n))+1):
            if (n%i) == 0:
                return False
        return True