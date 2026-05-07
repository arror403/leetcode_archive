class Solution:
    def digitCount(self, num: str) -> bool:
        num=list(map(int,str(num)))
        f=1
        for i in range(len(num)):
            if num[i] == num.count(i):
                continue
            else:
                f=0
                break
                
        if f:
            return 1
        else:
            return 0
            