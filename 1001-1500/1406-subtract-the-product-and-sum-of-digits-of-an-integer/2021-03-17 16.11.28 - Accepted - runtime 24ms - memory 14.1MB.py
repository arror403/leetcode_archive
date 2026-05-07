class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits=[]
        b=1
        while(1):
            if(n<10):
                digits.append(int(n))
                break
            else:
                digits.append(int(n%10))
                n/=10
        # print (digits)        
        a=sum(digits)
        # print(a)
        for i in digits:
            b=b*i
        # print(b)
        return b-a