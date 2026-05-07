class Solution:
    def minMaxDifference(self, num: int) -> int:
        nums=list(str(num))
        
        l=next((i for i in nums if i!='9'), '9')

        a=int(''.join('9' if i==l else i for i in nums))

        r=next((i for i in nums if i!='0'), '0')

        b=int(''.join('0' if i==r else i for i in nums))


        return a-b