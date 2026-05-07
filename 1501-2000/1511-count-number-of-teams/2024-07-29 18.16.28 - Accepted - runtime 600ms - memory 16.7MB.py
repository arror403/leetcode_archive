class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n=len(rating)
        res=0
        
        for j in range(1,n-1):
            l_smaller = sum(rating[i]<rating[j] for i in range(j))
            l_larger = j-l_smaller
            r_smaller = sum(rating[j]>rating[k] for k in range(j+1,n))
            r_larger = n-j-1-r_smaller
            
            res += l_smaller*r_larger + l_larger*r_smaller
        

        return res