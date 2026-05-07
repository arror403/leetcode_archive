class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=[str(i) for i in digits]
        digits=''.join(digits)
        digits=int(digits)
        digits+=1
        digits=list(map(int,str(digits)))
        return digits