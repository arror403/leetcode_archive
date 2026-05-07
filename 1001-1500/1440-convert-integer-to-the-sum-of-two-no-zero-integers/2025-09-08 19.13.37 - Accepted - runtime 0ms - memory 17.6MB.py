class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        tmp=0
        while '0' in str(1+tmp) or '0' in str(n-1-tmp): tmp+=1
                

        return [1+tmp, n-1-tmp]