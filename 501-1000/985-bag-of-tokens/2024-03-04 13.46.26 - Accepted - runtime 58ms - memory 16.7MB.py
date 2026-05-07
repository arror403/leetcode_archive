class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        res=0
        max_points=0
        tokens.sort()
        l,r=0,(len(tokens)-1)

        while(l<=r):
            if power>=tokens[l]:
                power-=tokens[l]
                res+=1
                l+=1
                max_points = max(max_points, res)
            elif res>=1:
                power+=tokens[r]
                res-=1
                r-=1
            else:
                break
        
        return max_points