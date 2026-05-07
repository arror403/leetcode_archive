class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        if '+-' in num1: num1=num1.replace('+-','-')
        if '+-' in num2: num2=num2.replace('+-','-')
        
        num1=num1.replace('i','j')
        num2=num2.replace('i','j')
        res=complex(num1)*complex(num2)
        
        return str(int(res.real))+'+'+str(int(res.imag))+'i'
        return 0