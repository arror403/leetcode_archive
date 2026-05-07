class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n=len(books)
        memo={}
        
        def dp(i):
            if i==n: return 0
            if i in memo: return memo[i]
            
            curr_width=curr_height=0
            res=inf
            
            for j in range(i,n):
                curr_width+=books[j][0]

                if curr_width>shelfWidth: break
                
                curr_height=max(curr_height, books[j][1])
                res=min(res, curr_height+dp(j+1))
            
            memo[i]=res

            return res
        
        
        return dp(0)