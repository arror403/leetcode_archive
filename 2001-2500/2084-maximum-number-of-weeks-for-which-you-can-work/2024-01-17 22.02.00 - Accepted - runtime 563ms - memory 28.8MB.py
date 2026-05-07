class Solution:
    def numberOfWeeks(self, m: List[int]) -> int:
        ##### power by chatGPT #####
        a=sum(m)
        b=max(m)
        return a if b*2<=a+1 else 2*(a-b)+1