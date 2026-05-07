class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        b=[]
        for i in A:
            if i%2==0:
                b.append(i)
        for i in A:
            if i%2==1:
                b.append(i)
                
        return b