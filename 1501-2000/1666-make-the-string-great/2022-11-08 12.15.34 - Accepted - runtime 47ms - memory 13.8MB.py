class Solution:
    def makeGood(self, s: str) -> str:
        s=list(s)
        
        while self.util(s):
            i=0
            while i < (len(s)-1):
                if abs(ord(s[i])-ord(s[i+1]))==32:
                    del s[i]
                    del s[i]
                i+=1

        return ''.join(s)


    def util(self,x):
        for i in range(len(x)-1):
            if abs(ord(x[i])-ord(x[i+1]))==32:
                return True
        return False