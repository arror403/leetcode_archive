class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        t=int(''.join([str(x) for x in digits]))+1
        
        return list(map(int,str(t)))