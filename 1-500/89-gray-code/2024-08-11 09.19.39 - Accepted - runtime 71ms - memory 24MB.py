class Solution:
    def grayCode(self, n: int) -> List[int]:
        i=0
        res=[]
        while i < (1<<n):
            # Generating the decimal values of gray code then using bitset 
            # to convert them to binary form
            res.append(i^(i>>1))
            i+=1

        return res