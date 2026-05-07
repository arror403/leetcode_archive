class Solution:
    def generateTheString(self, n: int) -> str:
        b=[]
        s=''
        if n%2==1:
            for i in range(n):s+='a'
        else:
            for i in range(n-1):s+='a'
            s+='b'
        return s