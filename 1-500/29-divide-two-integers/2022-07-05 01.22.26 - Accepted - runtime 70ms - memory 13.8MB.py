class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        r=int(dividend/divisor)
        
        if r<(-2147483648):
            return -2147483648
        elif r>2147483647:
            return 2147483647
        else:    
            return r