class Solution:
    def numberOfWeeks(self, m: List[int]) -> int:
        ##### power by chatGPT #####
        return sum(m) if max(m)*2<=sum(m)+1 else 2*(sum(m)-max(m))+1