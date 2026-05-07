class Solution:
    def convertToBase7(self, num: int) -> str:
        s=[]
        
        if num > 0:
            while num>=7:
                s.append(num%7)
                num=int(num/7)
            s.append(num)
            s.reverse()
            s=[str(i) for i in s]
            s=''.join(s)
            return s
        elif num < 0:
            num*=(-1)
            while num>=7:
                s.append(num%7)
                num=int(num/7)
            s.append(num)
            s.reverse()
            s=[str(i) for i in s]
            s.insert(0,'-')
            s=''.join(s)
            return s
            
        else:
            return "0"