class Solution:
    def smallestNumber(self, num: int) -> int:
        res=[]
        if num>=0:
            num=list(map(int,str(num)))
            num.sort()
            if 0 in num:
                for i in range(len(num)):
                    if num[i]==0: 
                        continue
                    else:
                        res.append(num[i])
                        del num[i]
                        break
            for i in num: res.append(i)
            return int(''.join(str(x) for x in res))
        elif num<0:
            num*=-1
            num=list(map(int,str(num)))
            num.sort()
            num.reverse()
            for i in num: res.append(i)
            return int(''.join(str(x) for x in res))*(-1)
            