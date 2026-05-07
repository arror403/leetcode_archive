class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        missing_sum=mean*(n+len(rolls))-sum(rolls)

        if missing_sum<n or missing_sum>6*n: return []
        
        base_value,remainder = divmod(missing_sum, n)
        res=[base_value]*n

        for i in range(remainder): res[i]+=1
        

        return res