class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        i=0
        f=False

        while i<len(s):
            if s[i]=='1':
                if f==False:
                    i+=1
                    continue
                else:
                    return False
            else:
                f=True
                i+=1


        return True