class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        M = max(candies)
        output=[]
        for i in range(0,len(candies)):
            if (candies[i]+extraCandies)>=M:
                # print((candies[i]+extraCandies))
                output.append(1)
            else:
                output.append(0)
            
        return output
                