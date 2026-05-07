class Solution:
    def isPalindrome(self, x: int) -> bool:
        f = 1
        b=[]
        if x<0:
            f = 0
        else:
            while x>=10:
                b.append(x%10)
                x=x//10
            b.append(x)
        # print(b)
        l=len(b)-1
        for i in range(len(b)):
            if (b[l]!=b[i]):
                f = 0
                break
            l=l-1
        return f