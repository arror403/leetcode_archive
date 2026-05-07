class Solution:
    def totalMoney(self, n: int) -> int:
        # w: week_count, r: remaining_days
        w, r = divmod(n, 7)
        
        # res = ((w*(w-1))//2)*7
        # res += w*28
        # res += ((r*(r+1))//2)+(w*r)


        return ((w*(w-1))//2)*7 + w*28 + ((r*(r+1))//2)+(w*r)