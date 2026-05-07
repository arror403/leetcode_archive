class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=int(''.join([str(i) for i in digits]))
        digits+=1
        return list(map(int,str(digits)))