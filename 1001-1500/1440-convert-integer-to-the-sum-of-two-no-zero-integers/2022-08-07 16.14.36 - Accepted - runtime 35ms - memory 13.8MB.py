class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        tmp=0
        while 1:
            if '0' in str(1+tmp) or '0' in str(n-1-tmp):
                tmp+=1
            else: break
                
        return [1+tmp,n-1-tmp]