class Solution:
    def countDigits(self, num: int) -> int:
      return len([i for i in list(map(int,str(num))) if num%i==0])