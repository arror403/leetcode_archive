class Solution:
    def romanToInt(self, s: str) -> int:
        b=[]
        sum=0
        for i in s:
            if i == 'I':
                b.append(1)
            elif i =='V':
                b.append(5)
            elif i =='X':
                b.append(10)
            elif i =='L':
                b.append(50)
            elif i =='C':
                b.append(100)
            elif i =='D':
                b.append(500)
            elif i =='M':
                b.append(1000)
        
        for j in range(0,len(b)-1):
            if b[j]<b[j+1]:
                sum-=b[j]
            else: 
                sum+=b[j]
        sum+=b[-1]
        return sum