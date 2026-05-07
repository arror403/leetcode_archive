class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        number=[int(i) for i in number]
        digit=int(digit)
        res=[]
        for i in range(len(number)):
            if number[i]==digit:
                tmp=list(number)
                del tmp[i]
                tmp=[str(x) for x in tmp]
                tmp=''.join(tmp)
                tmp=int(tmp)
                res.append(tmp)

        return str(max(res))
