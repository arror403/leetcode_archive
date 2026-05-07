class Solution:
    def makeGood(self, s: str) -> str:
        i=0
        s=list(s)

        while i<(len(s)-1):
            if abs(ord(s[i])-ord(s[i+1]))==32:
                del s[i:i+2]
                if i>0:  # Check if we can move one step back, to check the previous character
                    i-=1
            else:
                i+=1
        return ''.join(s)

        # while 1:
        #     flag=False
        #     if abs(ord(s[i])-ord(s[i+1]))==32:
        #         flag=True
        #         del s[i:i+2]

        #     i+=1

        #     if i==(len(s)-2):
        #         if flag:
        #             i=0
        #             continue
        #         else:
        #             return ''.join(s)