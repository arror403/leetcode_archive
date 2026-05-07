class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        r,res,index=1,[0]*num_people,0
        while 1:
            if candies>=r:
                res[index%num_people]+=r
                candies-=r
            else:
                res[index%num_people]+=candies
                break
            r+=1
            index+=1
            
        return res