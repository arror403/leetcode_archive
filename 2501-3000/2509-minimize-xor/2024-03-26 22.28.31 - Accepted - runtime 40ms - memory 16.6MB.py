class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count_1=bin(num2).count('1')
        res=''
        
        for x in bin(num1)[2:]:
            if x=='1' and count_1>0:
                res+='1'
                count_1-=1
            else:
                res+='0'

        if count_1==0: return int(res,2)

        elif count_1>0:
            res=list(res[::-1])
            i=0
            while count_1>0:
                if i>=len(res):
                    res.append('1')
                    count_1-=1
                elif res[i]=='0':
                    res[i]='1'
                    count_1-=1
                    i+=1
                else:
                    i+=1

            return int(''.join(res[::-1]),2)