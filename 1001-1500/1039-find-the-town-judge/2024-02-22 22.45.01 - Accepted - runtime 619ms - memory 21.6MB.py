class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust: return 1
        
        trust_counts=defaultdict(int)
        
        for a,b in trust:
            trust_counts[a]-=1  # a trusts someone
            trust_counts[b]+=1  # b is trusted by someone
        
        for person,count in trust_counts.items():
            if count==(n-1):
                return person
        
        return -1