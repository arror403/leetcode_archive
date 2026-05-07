class Solution:
    def hammingWeight(self, n: int) -> int:
        b=[]
        sum=0
        while n!=0:
            if n%2==1:
                b.append('1')
                n=int(n/2)
            elif n%2==0:
                b.append('0')
                n=int(n/2)
        # print (b)
        
        for i in b:
            if i == '1':
                sum+=1
                
        return sum