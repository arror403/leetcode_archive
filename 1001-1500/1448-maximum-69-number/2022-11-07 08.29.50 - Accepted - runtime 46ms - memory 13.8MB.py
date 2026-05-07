class Solution:
    def maximum69Number (self, num: int) -> int:
        num=list(map(int,str(num)))
        for i in range(len(num)):
            if num[i]==6:
                num[i]=9
                break
        return ''.join([str(i) for i in num])